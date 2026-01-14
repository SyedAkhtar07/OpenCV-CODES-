import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread("Photos/cats.jpg")
cv.imshow("cats",img)
print(img.shape)
blank=np.zeros(img.shape[:2],dtype="uint8")
mask=cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),100,255,-1)
# masked=cv.bitwise_and(img,img,mask=mask)
plt.figure()
plt.title("Rgb Histogram")
plt.xlabel("No of colors")
plt.ylabel("Color Intensity")

cols=["b",'g','r']
for i,col in enumerate(cols):
    hist=cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
cv.imshow("Masked Image",mask)
plt.show()
cv.waitKey(0) 
cv.destroyAllWindows()