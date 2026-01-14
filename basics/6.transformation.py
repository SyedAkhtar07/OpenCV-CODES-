import numpy as np
import cv2 as cv
def fn(frame,scale):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)
img=cv.imread("cat.jpg")
new=fn(img,.3)
cv.imshow("cat",new)
#translation
def translate(img,width,height):
    transmat=np.float32([[1,0,width],[0,1,height]])
    dim=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dim)
translaed=translate(new,100,100)
cv.imshow("new",translaed)
def rotation(img,angle,rotpot=None):
    (width,height)=img.shape[:2]
    if rotpot==None:
        rotpot=(width//2,height//2)
    rotpot=cv.getRotationMatrix2D(rotpot,angle,1.0)
    dim=(width,height)
    return cv.warpAffine(img,rotpot,dim)
rotated=rotation(new,-90)
cv.imshow("rotated",rotated)
#resize
resize=cv.resize(new,(700,400),interpolation=cv.INTER_CUBIC )
cv.imshow("Resized Image:",resize)
#flip
flip=cv.flip(new,-1)
cv.imshow("flip",flip)
cv.waitKey()
