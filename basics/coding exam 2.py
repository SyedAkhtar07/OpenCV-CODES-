import cv2 as cv
import numpy as np
img=cv.imread(r"F:\Akhtar study\Python\PyProjects\new\advanced\Photos\cats.jpg")
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
lower=np.array([35,0,55])
higher=np.array([85,255,255])
mask=cv.inRange(hsv,lower,higher)
cv.imshow("Mask Image",mask)
new=cv.bitwise_not(mask)
final=cv.bitwise_and(img,img,mask=new)
cv.imshow("final",final)
cv.waitKey()