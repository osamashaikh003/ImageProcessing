import cv2

img=cv2.imread('C:/Users/DELL/Downloads/cloud.jpg',1)

cv2.imshow('Original Image',img)

image2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imwrite('Image1.jpg',image2)

cv2.imshow('Grayscale Image',image2)

cv2.waitKey(5)
