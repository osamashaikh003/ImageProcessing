import cv2

img=cv2.imread('C:/Users/DELL/Downloads/cloud.jpg',1)

img1=img.copy()

name=cv2.putText(img1,'IOCT',(50,70),cv2.FONT_HERSHEY_COMPLEX,2,(227,245,220),2)
cv2.imshow('Name on Image',name)

cv2.waitKey(3)
