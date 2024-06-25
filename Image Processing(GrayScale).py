import cv2

image=cv2.imread('C:/Users/DELL/Downloads/scenery2.jpg') # You can also use num for GRAYSCALE (0) to directly put gray backgound in photo

img1=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale", img1)
