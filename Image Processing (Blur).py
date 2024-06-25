import cv2

image=cv2.imread('C:/Users/DELL/Downloads/scenery2.jpg')
cv2.imshow('Original Image',image)

filter1=cv2.GaussianBlur(image,(7,7),0)
cv2.imshow('Gaussian Blur',filter1)

filter2=cv2.medianBlur(image,9)
cv2.imshow('Median Blur',filter2)

filter3=cv2.blur(image,(9,9))
cv2.imshow('Averaging Blur',filter3)

