import numpy as np
import cv2

img1 = cv2.imread( "Bug.bmp", 0 )
thresh, img2 = cv2.threshold( img1, 127, 255, 
               cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU )
print( "Threshold =", thresh )
cv2.imshow( "Original Image",  img1 )	
cv2.imshow( "Thresholding", img2 )
cv2.waitKey( 0 )