import cv2

img=cv2.imread('C:/Users/DELL/Downloads/scenery2.jpg')

edge=cv2.Canny(img,100,200)
cv2.imshow('Edge Detection',edge)

cv2.waitKey()
