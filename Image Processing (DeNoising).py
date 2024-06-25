import cv2

img=cv2.imread("C:/Users/DELL/Downloads/Noisy Image1.jpg")

cv2.imshow('Original Image',img)

img1=cv2.fastNlMeansDenoising(img,None,10,7,21) 
cv2.imshow('Denoise Image',img1)

cv2.waitKey(0)
