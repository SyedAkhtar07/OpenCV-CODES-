import cv2 as cv
def fn(img,scale=.4):
    width=int(img.shape[1]*scale)
    height=int(img.shape[0]*scale)
    dim=(width,height)
    return cv.resize(img,dim,interpolation=cv.INTER_AREA)
img=cv.imread("cat.jpg")
newimg=fn(img,.3)
cv.imshow("Cat Resized",newimg)
vd=cv.VideoCapture("arav.mp4")
#ie vd=cv.videocapture(0) you can give this command when you need it to record your webcam
while True:
    isTrue,frame=vd.read()
    cv.imshow("Video:",fn(frame))
    if(cv.waitKey(20) & 0xFF==ord('x')):
        break
vd.release()
cv.destroyAllWindows()