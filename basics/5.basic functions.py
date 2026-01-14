import cv2 as c
def fn(frame,scale):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return c.resize(frame,dim,interpolation=c.INTER_AREA)
ig=c.imread("cat.jpg")
img=fn(ig,.2)
c.imshow('cat',img)
#bgr to gray scale
grey=c.cvtColor(img,c.COLOR_BGR2GRAY)
c.imshow('graycat',grey)
#Blur the image it helps in finding the edges in axn image 
blur=c.GaussianBlur(img,(7,7),c.BORDER_DEFAULT)
c.imshow('blur',blur)
#canny edge determining the edge 
cany=c.Canny(img,125,175) #125 and 180 are the threshold e in which it is medium if 175+ it is suitable for maximum purpose
c.imshow('Canny edge',cany)
#dilate means to brighten the edges and thick it
dilated = c.dilate(cany, (7,7), iterations=3)#(15,15) is kernel which should be odd
c.imshow('Dilatededge',cany)
#erodeing means again lightening the dilation and 
eroded = c.erode(dilated, (7,7), iterations=3)
c.imshow('eroded',eroded)
#resizing and croping
resized = c.resize(img, (300,150), interpolation=c.INTER_CUBIC)
c.imshow("Resized",resized)
crop=img[100:300,200:400]
c.imshow("Cropped",crop)
c.waitKey()