import cv2

img=cv2.imread('C:/Users/DELL/Downloads/scenery2.jpg',1)

circle=cv2.circle(img,(100,200),60,(0,0,24),-1)

cv2.imshow('Circle',circle)

cv2.waitKey()
