import cv2

img=cv2.imread('C:/Users/DELL/Downloads/scenery2.jpg',1)

rotation=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('ROTATION CLOCKWISE',rotation)

cv2.waitKey()
