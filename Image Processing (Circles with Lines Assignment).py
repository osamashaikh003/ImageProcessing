import cv2
import numpy as np

img=cv2.imread("C:/Users/DELL/Downloads/Circle with line 4.png")
#img2=cv.imread("C:/Users/DELL/Downloads/Circles with Line 2.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

edge=cv2.Canny(gray,50,150)

lines=cv2.HoughLines(edge,1,np.pi/180,200)

for r_theta in lines:
    arr=np.array(r_theta[0],dtype=np.float64)
    r,theta=arr

    a=np.cos(theta)
    b=np.sin(theta)

    x0=a*r
    y0=b*r

    x1=int(x0+1000*(-b))
    y1=int(y0+1000*(a))
    x2=int(x0-1000*(-b))
    y2=int(y0-1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(110,0,0),2)


# Circle

blur=cv2.blur(gray,(3,3))

circles=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,10,param1=10,param2=30,minRadius=5,maxRadius=50)

if circles is not None:
    dcircle=np.uint16(np.around(circles))
    for i in dcircle[0,:]:
        x,y,r=i[0],i[1],i[2]
        cv2.circle(img,(x,y),r,(0,0,255),2)

cv2.imshow('Circles with Lines', img)

cv2.waitKey()
