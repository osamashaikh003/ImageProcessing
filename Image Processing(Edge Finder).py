import cv2

video=cv2.VideoCapture("C:/Users/DELL/Downloads/SampleVideo_1280x720_1mb.mp4")

while(video.isOpened()):
    res,frame=video.read()
    frame=cv2.resize(frame,(540,380),fx=0,fy=0)

    cv2.imshow('Frame',frame)

    edge=cv2.Canny(frame,100,200)
    cv2.imshow('Edge',edge)

    if cv2.waitKey(25)& 0xFF==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
