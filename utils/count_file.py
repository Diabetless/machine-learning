# script for counting how many images have been labeled

import os
# change with your directory path
os.chdir(os.path.join("D:\\","Tugas","Bangkit","Dataset","Resized","test"))
# change the food according to your need
food="salad"
files=[]
for i in range(1000):
    # append to files only if .txt file of that name exists
    if(os.path.exists("{}_{}.txt".format(food,str(i)))):
        files.append("{}_{}.jpg".format(food,str(i)))
print(files)
# count how many images have been labeled
print(len(files))