import cv2

img=cv2.imread("C:/Users/DELL/Downloads/Noisy Image 2 colored.png")

cv2.imshow('Original Image',img)

img1=cv2.fastNlMeansDenoisingColored(img,None,10,10,21) 
cv2.imshow('Denoise Image',img1)

cv2.waitKey(0)
