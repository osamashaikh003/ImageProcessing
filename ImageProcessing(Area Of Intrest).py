import cv2
img=cv2.imread('C:/Users/DELL/Downloads/scenery2.jpg',1)

cv2.imshow('Image',img)

roi=img[100:300,200:400]

cv2.imshow('Area of Intrest',roi)

cv2.waitKey(3)
