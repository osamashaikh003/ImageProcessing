import cv2

import numpy as np

image=cv2.imread('C:/Users/DELL/Downloads/scenery2.jpg',0)
image=cv2.resize(image,(600,600))


cv2.imshow('Original Image', image)

kernel=np.ones((5,5),np.uint8)

er1=cv2.erode(image,kernel)
cv2.imshow("Erode mode",er1) # Erode mode Reduces pixel from edges of images within given array zones 


er2=cv2.dilate(image,kernel)
cv2.imshow("Dilate mode", er2) # Dilate mode adds extra pixel from edges of image within given array zones


cv2.waitKey(0)
