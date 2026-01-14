import cv2 as cv
img=cv.imread("Photos/cats.jpg")
blur=cv.blur(img,(3,3))
cv.imshow("Average blur",blur)
#Gaussian blur
gaus=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("Gaussian Blur",gaus)
#Median blur
med=cv.medianBlur(img,3)
cv.imshow("Median Blur",med)
#Bilateral blur
bil=cv.bilateralFilter(img,11,30,25)
cv.imshow("Bilateral Blur",bil)
cv.waitKey()