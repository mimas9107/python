import numpy as np
import cv2

img = cv2.imread( "Script.bmp", 0 )
thresh, img1 = cv2.threshold( img, 128, 255, cv2.THRESH_BINARY )
img2 = cv2.adaptiveThreshold( img, 255, 
	   cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 0 )
img3 = cv2.adaptiveThreshold( img, 255, 
	   cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0 )
cv2.imshow( "Original Image",  img )	
cv2.imshow( "Global Thresholding", img1 )
cv2.imshow( "Adaptive Thresholding(Mean)", img2 )
cv2.imshow( "Adaptive Thresholding(Gaussian)", img3 )
cv2.waitKey( 0 )