import cv2 as cv
img=cv.imread("cats.jpg")
cv.imshow("cat in Bgr",img)
#to gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray cat",gray)
#to rgb
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("Rgb Cat",rgb)
#to lab
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab cat",lab)
#from rgb to bgr
bgr=cv.cvtColor(rgb,cv.COLOR_RGB2BGR)
cv.imshow("BGR cat",bgr)
#Like that we can convert any color to any other color spaces but if it not change it to another to convert it

cv.waitKey()
