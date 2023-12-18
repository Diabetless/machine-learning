# Food Object Detection

This repository contains the creation of an object detection feature using a pre-trained YOLO model. The main components of this feature are encapsulated in a Jupyter Notebook **(Model.ipynb)**.

## Folder Structures
Before delving into the code, it's crucial to grasp the project's folder arrangement. Below is a broad summary of the directory layout.
```bash
object_recognition
├───assets              # Static assets (image, etc) for README.
├───images              # Store images file to used in prediction demo
├───model               # Food object detection model in TFjs converted format
├───utils               # Utility and helper scripts to preprocess the dataset
├───classes.json        # List of classes/labels name
├───Model.ipynb         # Encapsulated model creation steps
└───predict.js          # Prototype of deployed model API
```

## Datasets
We use Food Image datasets from kaggle which contain 11 classes of images :
<img src='./assets/dataset_images.png' alt='Dataset Image' width=100% />

The datasets labelled using LabelImg with 3 splits (train, test, val) package and saved as **.zip** file in **[datasets.zip](https://drive.google.com/file/d/186HlpFc60T0jWYrJPodAJNtYK6Hgr2tg/view?usp=sharing)**


## Getting Started
You can try the demo of Food Object detection model using Tensorflowjs-node as server side prediction process.

### Prerequisites
- [Nodejs](https://nodejs.org/en) v18.12.0 or above 
- [NPM](https://www.npmjs.com/)
- [TFjs-node](https://www.npmjs.com/package/@tensorflow/tfjs-node)

### Installation
1. Fork to your github and Clone the repository
```shell
git clone https://github.com/<your_github_username>/machine-learning.git
```
2. Install the dependencies needed
```
npm install
```

### Usage
1. Change working directory to ```object_recognition```
```shell
cd object_recognition
```
2. Copy your image to [images](./images/) folder
3. Run the code with added argument
```
node predict.js [IMAGE_FILEPATH]
```
3. The results will be array of classes that detected in the image.

### Example
Prediction using ```test-image.jpg```
```
node predict.js ./images/test-image.jpg
```
Example result
```javascript
[ 'noodles', 'french fries', 'hamburger' ]
```
