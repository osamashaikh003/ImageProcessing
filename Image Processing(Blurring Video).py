import cv2

video=cv2.VideoCapture("C:/Users/DELL/Downloads/SampleVideo_1280x720_1mb.mp4")


while(video.isOpened()):
    res,frame=video.read()
    frame=cv2.resize(frame,(540,380),fx=0,fy=0)

    cv2.imshow('Frame',frame)

    blur=cv2.GaussianBlur(frame,(7,7),0)
    cv2.imshow('Blur',blur)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

video.releae()
cv2.destroyAllWindows()
    
