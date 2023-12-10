# script for deleting files that are not labeled

import os
# change with your directory path
os.chdir(os.path.join("D:\\","Tugas","Bangkit","Dataset","Resized","test"))
# change the food according to your need
food="salad"
# looping from 0 to 1000 because every food dataset has 1000 images from food_0 to food_999
for i in range(1000):
    # delete only images that don't have .txt file with the same name
    if(not(os.path.exists("{}_{}.txt".format(food,str(i))))):
        # uncomment the line below and comment the os.remove line first to check if the targeted images are correct
        # print("{}_{}.jpg".format(food,str(i)))
        os.remove("{}_{}.jpg".format(food,str(i)))