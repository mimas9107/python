# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:32:58 2024

@author: user
"""

import numpy as np
import cv2


file='Breakfast.bmp'
img=cv2.imread(file,-1)

x,y=eval(input("enter window(x,y):"))
w,h=eval(input("enter window(w,h) for ROI:"))

ROI=img[y:y+h, x:x+w, :].copy()

cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)

text='Latte'
ROI_r=np.zeros_like(ROI)
ROI_g=np.zeros_like(ROI)
ROI_b=np.zeros_like(ROI)

ROI_r[:,:,2]=ROI[:,:,2]
ROI_g[:,:,1]=ROI[:,:,1]
ROI_b[:,:,0]=ROI[:,:,0]

cv2.putText(img, text, (x-5,y-5), cv2.FONT_HERSHEY_PLAIN, 2.0, color=(255,0,0), thickness=2)

cv2.imshow("orig:",img)

cv2.imshow("ROI:",ROI)
cv2.imshow("ROI_r:",ROI_r)
cv2.imshow("ROI_g:",ROI_g)
cv2.imshow("ROI_b:",ROI_b)
cv2.waitKey(0)

cv2.destroyAllWindows()