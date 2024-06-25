import cv2

img =cv2.imread("C:/Users/DELL/Downloads/scenery2.jpg",0)
cv2.imshow('original',img)

th,res=cv2.threshold(img,130,255,cv2.THRESH_BINARY)
cv2.imshow("Thresh Binary",res)

th,res1=cv2.threshold(img,130,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh Binary Invert",res1)


th,res2=cv2.threshold(img,130,255,cv2.THRESH_TRUNC)
cv2.imshow("Thresh Truncate",res2)

th,res3=cv2.threshold(img,130,255,cv2.THRESH_TOZERO)
cv2.imshow("Thresh ToZERO",res3)

th,res4=cv2.threshold(img,130,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("Thresh ToZERO Invert",res4)

cv2.waitKey()
