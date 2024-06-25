import cv2
import numpy as np

img=cv2.imread("C:/Users/DELL/Downloads/Chess Board.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corner=cv2.goodFeaturesToTrack(gray,25,0.01,10)

corner=np.int32(corner)


for i in corner:
    x,y=i.ravel()
    cv2.circle(img,(x,y),3,(0,0,255),-1)

cv2.imshow('Corner Finder',img)
