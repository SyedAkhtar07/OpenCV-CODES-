import cv2 as cv
img=cv.imread("cat.jpg")
cv.imshow("cat",img)
vd=cv.VideoCapture("arav.mp4")
#ie vd=cv.videocapture(0) you can give this command when you need it to record your webcam
while True:
    isTrue,frame=vd.read()
    cv.imshow("Video:",frame)
    if(cv.waitKey(10) & 0xFF==ord('x')):
        break
vd.release()
cv.destroyAllWindows()
