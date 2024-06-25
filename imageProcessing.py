import cv2
img=cv2.imread('C:/Users/DELL/Downloads/cloud.jpg',1)
'''
1 = Color Picture
0 = Grayscale
'''

cv2.imshow('image',img)

cv2.waitKey(3) 
