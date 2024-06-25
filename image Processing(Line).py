import cv2

img=cv2.imread('C:/Users/DELL/Downloads/scenery2.jpg',1)

line=cv2.line(img,(10,5),(800,150),(0,0,45),5)

cv2.imshow('Line',line)

cv2.waitKey()
