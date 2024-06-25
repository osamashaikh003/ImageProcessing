import cv2

img=cv2.imread('C:/Users/DELL/Downloads/cloud.jpg',1)

h,w=img.shape[:2]

print("Height: ",h)
print("Width: ",w)


(b,g,r)=img[100,100]

print("Blue: ",b)
print("Green: ",g)
print("Red: ",r)


cv2.waitKey(3)
