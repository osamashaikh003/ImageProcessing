import cv2

img=cv2.imread("people1.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

haar=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces=haar.detectMultiScale(gray,1.1,9,minSize=(60,60))

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('Face Detected', img)

cv2.waitKey(0)
