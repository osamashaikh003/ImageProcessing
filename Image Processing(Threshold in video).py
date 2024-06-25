import cv2
import os

video=cv2.VideoCapture("C:/Users/DELL/Downloads/SampleVideo_1280x720_2mb.mp4")

while(video.isOpened()):
    res,frame=video.read()
    frame=cv2.resize(frame,(540,380),fx=0,fy=0)

    cv2.imshow("Frame",frame)

    tra=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    thresh=cv2.adaptiveThreshold(tra,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)

    cv2.imshow("Thresh",thresh)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
