import cv2

video=cv2.VideoCapture(0)

while(True):
    ret,res=video.read()
    cv2.imshow("Frame",res)

    cv2.waitKey(0)

video.release()
