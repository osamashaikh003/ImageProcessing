import os
import cv2
from PIL import Image

print(os.getcwd())

os.chdir("C:/Users/DELL/AppData/Local/Programs/Python/Python312/Image Processing/Images")
path="C:/Users/DELL/AppData/Local/Programs/Python/Python312/Image Processing/Images"

mean_height=0
mean_width=0

no_images=len(os.listdir("."))

for file in os.listdir("."):
    im=Image.open(os.path.join(path,file))
    width,height=im.size
    mean_height+=height
    mean_width+=width

mean_width=int(mean_width/no_images)
mean_height=int(mean_height/no_images)

for file in os.listdir('.'):
    im=Image.open(os.path.join(path,file))
    width,height=im.size
    resize=im.resize((mean_width,mean_height),Image.ADAPTIVE)
    resize.save(file,'JPEG',quality=95)
    print(im.filename.split('\\')[-1],'is Resized')


def generate_video():
    img_folder="C:/Users/DELL/AppData/Local/Programs/Python/Python312/Image Processing/Images"
    video_name="Video1.avi"
    os.chdir("C:/Users/DELL/AppData/Local/Programs/Python/Python312/image processing/")

    images=[img for img in os.listdir(img_folder) if img.endswith('.jpg') or img.endswith('.jpeg') or img.endswith('.png') or img.endswith('.jfif')]

    frame=cv2.imread(os.path.join(img_folder,images[0]))

    height,width,layer=frame.shape

    video=cv2.VideoWriter(video_name,0,1,(width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(img_folder,image)))

    cv2.destroyAllWindows()

    video.release()

generate_video()
            
