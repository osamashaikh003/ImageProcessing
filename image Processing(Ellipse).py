import cv2

img=cv2.imread('C:/Users/DELL/Downloads/scenery2.jpg',1)

ellipse=cv2.ellipse(img,(250,150),(100,40),0,0,360,(0,0,225),1)

cv2.imshow('Ellipse',ellipse)

cv2.waitKey()
