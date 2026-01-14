import cv2 as cv
import numpy as np
img=cv.imread("Photos/cats.jpg")
cv.imshow("Cats",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
t,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow("Thresh Image",thresh)
t,inv=cv.threshold(gray,125,255,cv.THRESH_BINARY_INV)
cv.imshow("Inverse Thresh",inv)
#Adaptive Thresholding
ad=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("Adaptive Thresh",ad)#if you want to inverse what you see you must change the type
cv.waitKey(0)