const tf = require('@tensorflow/tfjs-node');
const classes = require('./classes.json');
const fs = require('fs').promises;

const loadModel = async () => {
  const modelFile = tf.io.fileSystem('./model/model.json');
  const model = await tf.loadGraphModel(modelFile);
  return new Promise((resolve) => {
    resolve(model);
  });
};

const preProcess = async (image) => {
  try {
    const buf = await fs.readFile(image);
    const preprocessedData = tf.tidy(() => {
      const data = tf.node.decodeImage(buf);
      const resizedData = tf.image.resizeBilinear(data, [512, 512]);
      const normalizedData = tf.div(resizedData, 255.0);
      const selectionType =
        normalizedData.shape[2] === 4
          ? normalizedData.slice([0, 0, 0], [512, 512, 3])
          : normalizedData;
      return selectionType.expandDims(0).transpose([0, 3, 1, 2]);
    });

    return new Promise((resolve) => {
      resolve(preprocessedData);
    });
  } catch (err) {
    console.error(err);
  }

  return null;
};

const postProcess = async (res) => {
  const boxes = tf.tidy(() => {
    const h = res.slice([0, 3, 0], [1, 1, -1]);
    const w = res.slice([0, 2, 0], [1, 1, -1]);
    const y1 = res.slice([0, 1, 0], [1, 1, -1]).sub(tf.div(h, 2));
    const x1 = res.slice([0, 0, 0], [1, 1, -1]).sub(tf.div(w, 2));

    return tf
      .concat([y1, x1, y1.add(h), x1.add(w)])
      .transpose()
      .squeeze();
  });

  const [scores, labels] = tf.tidy(() => {
    const confClasses = res.slice([0, 4, 0], [1, classes.length, -1]).transpose().squeeze();
    return [confClasses.max(1), confClasses.argMax(1)];
  });

  const nonMaxSupression = await tf.image.nonMaxSuppressionAsync(boxes, scores, 5, 0.7, 0.5);
  const detectedObject = tf.tidy(() => {
    const uniques = tf.unique(labels.gather(nonMaxSupression));
    return uniques.values.arraySync();
  });
  const stringClasses = detectedObject.map((idx) => classes[idx]);

  console.log(stringClasses);

  tf.dispose([boxes, scores, labels, nonMaxSupression]);
};

const main = async () => {
  const imagePath = process.argv[2];
  const model = await loadModel();
  const gambar = await preProcess(imagePath);

  if (gambar === null) {
    console.log('Image Not Found!');
    return;
  }

  const res = await model.predict(gambar);

  await postProcess(res);

  tf.dispose([res, gambar, model]);
};

main();
