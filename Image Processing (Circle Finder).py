import cv2
import numpy as np

img=cv2.imread("C:/Users/DELL/Downloads/Round Pebble.webp")

gray=(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))

blur=cv2.blur(gray,(3,3))

circles=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=5,maxRadius=35)

if circles is not None:
    dcircle=np.uint16(np.around(circles))
    for i in dcircle[0,:]:
      x,y,r=i[0],i[1],i[2]
      cv2.circle(img,(x,y),r,(0,144,0),2)

cv2.imshow('Circles',img)
cv2.waitKey(0)
      
