# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:16:34 2024

@author: user
"""
import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    x, y = y, x
    if(img.ndim !=3):
        print("(x,y)=(%d, %d)"%(x,y),end=" ")
        print("Gray-level=%3d"%img[x,y])
    else:
        print("(x,y=(%d, %d)"%(x,y),end=" ")
        print("(R,G,B)=(%3d,%3d,%3d)"%(img[x,y,2],img[x,y,1],img[x,y,0]))

img=cv2.imread('Breakfast.bmp')
cv2.namedWindow('test1')
cv2.setMouseCallback('test1', onMouse)

cv2.imshow("test1",img)

cv2.waitKey(0)

cv2.destroyAllWindows()