import cv2

img=cv2.imread("C:/Users/DELL/Downloads/scenery2.jpg",0)

cv2.imshow('Original Image',img)

th1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('Adaptive Thresh MEAN',th1)


th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('Adaptive Thresh GAUSSIAN',th2) 


th,res=cv2.threshold(img,None,255,cv2.THRESH_OTSU)
print(th)
cv2.imshow('Thresh OTSU',res)

cv2.waitKey()
