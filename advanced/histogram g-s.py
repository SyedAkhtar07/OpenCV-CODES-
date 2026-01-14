import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread("Photos/cats.jpg")
cv.imshow("cats",img)
print(img.shape)
blank=np.zeros(img.shape[:2],dtype="uint8")
circle=cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),100,255,-1)

#For gray scale images
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
mask=cv.bitwise_and(gray,gray,mask=circle)
cv.imshow("Gray cats",mask)
hist=cv.calcHist([gray],[0],mask,[256],[0,256])
plt.figure()
plt.title("Gray Cats Histogram")
plt.xlabel("Colors")
plt.ylabel("Pixel Intensity")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)