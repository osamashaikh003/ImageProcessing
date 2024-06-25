import cv2

video=cv2.VideoCapture(0)

while(True):
    ret,res=video.read()
    #cv2.imshow('Frame',res)


    gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

    haar=cv2.CascadeClassifier('haarCascade_frontalface_default.xml')

    faces=haar.detectMultiScale(gray,1.1,9,minSize=(30,30))

    for (x,y,w,h) in faces:
        cv2.rectangle(res,(x,y),(x+w,y+h),(2,255,0),2)

    cv2.imshow('Webcam Face Detection',res)

    if cv2.waitKey(10) & 0xFF==ord('q'):
        break


video.release()
cv2.destroyAllWindows()


