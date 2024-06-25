import os
import cv2

video=cv2.VideoCapture("C:/Users/DELL/Downloads/SampleVideo_1280x720_1mb.mp4")

try:
    if not os.path.exists("data"):
        os.makedirs("data")

except OSError:
    print("Error in folder creation")

cur_frame=0
          
while(True):
    res,frame=video.read()
    if res:
        name="./data/frame"+str(cur_frame)+".jpg"
        print("Creating ",name)
        cv2.imwrite(name,frame)
        cur_frame+=1
    else:
        break

video.release()
cv2.destroyAllWindows()
