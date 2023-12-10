# Food Object Detection

This repository contains the creation of an object detection feature using a pre-trained YOLO model. The main components of this feature are encapsulated in a Jupyter Notebook **(Model.ipynb)**.

## Folder Structures
- [Model/](./model/)
- [Utils/](./utils/)
- [Images/](./images/)

## Datasets
We use Food Image datasets from kaggle which contain 11 classes of images :
- Apple
- Avocado
- Cake
- Cooked Chicken
- Dragonfruit
- French Fries
- Fried Rice
- Hamburger
- Noodles
- Omelette
- Salad

The datasets labelled using LabelImg with 3 splits (train, test, val) package and saved as **.zip** file in **[datasets.zip](https://drive.google.com/file/d/186HlpFc60T0jWYrJPodAJNtYK6Hgr2tg/view?usp=sharing)**

## Model
The model has trained using pre-trained ***YOLOv8m*** model on the custom datasets on our datasets. The result of model stored in **.json** format and sharded **.bin** file.

## Utils
Utils folder contain python scripts to preprocess the datasets.


## Getting Started
You can try the demo of Food Object detection model using Tensorflowjs-node as server side prediction process.

### Prerequisites
- Python 3.9
- Pip3
- Nodejs
- Tfjs-node

### Installation
1. Fork to your github and Clone the repository
``` 
git clone https://github.com/<your_github_username>/machine-learning.git
```
2. Install the dependencies needed
```
npm install
```

### Usage
1. Copy your image to [images](./images/) folder
2. Run the code with added argument
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