import cv2 as c
import numpy as np
blank=np.zeros((500,500,3),dtype='float32')
#To paint in certain colour
blank[:]=255,255,255
#To draw a rectangle in it
c.rectangle(blank,(100,200),(400,300),(0,0,255),thickness=-1)

#To draw circle
c.circle(blank,(250,250),20,(0,0,0),thickness=-1)

c.line(blank,(100,200),(400,300),(255,0,0),thickness=3)
c.line(blank,(400,200),(100,300),(255,0,0),thickness=3)

c.putText(blank,"Hello This is Akhtar",(50,100),c.FONT_HERSHEY_TRIPLEX,1.0,(0,0,0),2)
c.imshow('Rectangle',blank)
c.waitKey(0)

