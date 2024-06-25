import cv2

video=cv2.VideoCapture("C:/Users/DELL/Downloads/3571264-uhd_3840_2160_30fps.mp4")

while(video.isOpened()):
    ret,frame=video.read()

    if ret==True:
        cv2.imshow("Video",frame)
        if cv2.waitKey(25) & 0xFF==ord('q'): # 0xFF means 255
            break

    else:
        break

video.release()
cv2.destroyAllWindows()
