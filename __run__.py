import cv2 as cv
import numpy as np
import webbrowser, os
import subprocess
from google_images_download import google_images_download  

print("Search for an object?>>")
keywords = input()

response = google_images_download.googleimagesdownload()

keywords = keywords + " image with black background"
arguments = {"keywords":keywords,"limit":1,"print_urls":True}
paths = response.download(arguments)
print(paths)

path = 'C:\\Users\\AkaiShuichi\\AnacondaSavedFiles\\downloads'

files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))

if files:
    imgpath = files[0]
    

imgl = cv.imread(imgpath,0)

#decreasing image resolution in equal ratio
oheight = imgl.shape[0]
owidth = imgl.shape[1]

if owidth>oheight:
    width = 350
    height = (oheight * width)//owidth

else:
    height = 350
    width = (owidth * height)//oheight

img = cv.resize(imgl,(int(width),int(height)))
smooth = cv.blur(img,(5,5))

obj = open('C://Users//AkaiShuichi//Documents//GitHub//saiavinashdamera.github.io//assets//object.obj','w+')

obj.write("# Created for mini project - OBJ File\n")
obj.write("# 509\n\n")
obj.write('o customobject.obj\n')


#format(img[y][x],img[y][x+1],img[y+1][x],img[y+1][x+1])
# average = np.average(smooth)

def estimate(x):
#     if x > average: return int(average)
#     if x > 50 and x<100: return x//3
#     elif x >100 and x<150: return x//4
#     elif x >150 and x<200: return x//5
#     elif x>200 and x<255: return x//6   
#     else: return x//2
    
    return x/2

for i in range(0,height):
    for j in range(0,width):
        obj.write("v {} {} {} \n".format(float(i),float(j),int(estimate(smooth[i][j]))))    
     
obj.write("\n\n\n") 
obj.write("#faces for the obj file\n") 
obj.write("usemtl None\ns off\n") 

ar = np.zeros(shape=(height,width))

k=0
for i in range(0,height):
    for j in range(0,width):
        k=k+1
        ar[i][j]=k

         
for i in range(0,height-1):
    for j in range(0,width-1):
        obj.write("f {} {} {} {} \n".format(int(ar[i][j]),int(ar[i+1][j]),int(ar[i+1][j+1]),int(ar[i][j+1])))
        #print(ar[i][j],ar[i+1][j],ar[i][j+1],ar[i+1][j+1])
        

obj.close()

print("object formed successfully! at path C://Users//AkaiShuichi//Documents//GitHub//saiavinashdamera.github.io//assets//object.obj")
print("Please try to view it in a .obj parser")