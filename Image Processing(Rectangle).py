import cv2

img=cv2.imread('C:/Users/DELL/Downloads/cloud.jpg',1)

img1=img.copy()

rectangle=cv2.rectangle(img1,(10,20),(200,100),(227,245,220),2)
cv2.imshow('Rectangle on Image',rectangle)

cv2.waitKey(3)
