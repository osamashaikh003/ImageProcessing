import cv2

img=cv2.imread('C:/Users/DELL/Downloads/scenery2.jpg',1)

cv2.imshow('Image',img)

resize=cv2.resize(img,(800,400))

cv2.imshow('Resize Image',resize)

cv2.waitKey(0)
