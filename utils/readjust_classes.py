# script for changing every index to suit the full classes.txt file

import os
# change with your directory path
os.chdir(os.path.join("D:\\","Tugas","Bangkit","Dataset","Resized","test"))
# change the list of foods according to the name of images that you labeled (ex: hamburger, french_fries, etc.)
foods=["noodles","omelette","salad"]
content=[]
temp=''
for food in foods:
    for i in range(1000):
        if(os.path.exists("{}_{}.txt".format(food,str(i)))):
            # open the file with read mode
            with open("{}_{}.txt".format(food,str(i)),"r") as file:
                # read every line in the file one by one
                for line in file:
                    # change every first character (which is the index) to suit the full classes.txt
                    # for example, noodles had index 0 at first, but in the full classes.txt it should be 8
                    if(line[0]=='0'):
                        temp='8'
                    elif(line[0]=='1'):
                        temp='5'
                    elif(line[0]=='2'):
                        temp='9'
                    elif(line[0]=='3'):
                        temp='7'
                    elif(line[0]=='4'):
                        temp='10'
                    # add the revised string to content
                    content.append(temp+line[1:])
            # open the file with write permission
            with open("{}_{}.txt".format(food,str(i)),"w") as file:
                # rewrite the content of the file
                for line in content:
                    file.write(line)
            # reset the content list to empty every time we finish rewriting a file
            content=[]

