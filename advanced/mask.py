import cv2 as cv
import numpy as np
img=cv.imread("Photos/cats.jpg")
blank=np.zeros(img.shape[:2],dtype="uint8")
print(img.shape)
rect=cv.rectangle(blank.copy(),(75,50),(570,370),255,-1)
cir=cv.circle(blank.copy(),(300,200),200,255,-1)
andd=cv.bitwise_and(img,img,mask=cv.bitwise_or(rect,cir))
cv.imshow("Masked",andd)
cv.waitKey()
