import cv2

image=cv2.imread('C:/Users/DELL/Downloads/scenery2.jpg')
image=cv2.resize(image,(600,600))
cv2.imshow("Original Image",image)


image=cv2.copyMakeBorder(image,8,8,8,8,cv2.BORDER_REFLECT)

image=cv2.resize(image,(600,600))
cv2.imshow("Bordered Image",image)
