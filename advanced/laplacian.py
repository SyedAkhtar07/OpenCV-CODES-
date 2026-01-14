import cv2 as cv
import numpy as np
img=cv.imread("Photos/park.jpg")
cv.imshow("Park",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#Laplacian (Have some noise)
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
#Sobel
sx=cv.Sobel(gray,cv.CV_64F,1,0)
sy=cv.Sobel(gray,cv.CV_64F,0,1)
orr=cv.bitwise_or(sy,sx,)
cv.imshow("laplacian",lap)
cv.imshow("Sobel",orr)
cv.imshow("Canny",cv.Canny(gray,125,175))
cv.waitKey(0)