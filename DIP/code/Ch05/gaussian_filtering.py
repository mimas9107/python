import numpy as np
import cv2

img1 = cv2.imread( "Lenna.bmp", -1 )
img2 = cv2.GaussianBlur( img1, ( 11, 11 ), 0 )
img3 = cv2.GaussianBlur( img1, ( 11, 11 ), 25 )
img4 = cv2.GaussianBlur( img1, ( 11, 11 ), 50 )
cv2.imshow( "Original Image", img1 )	
cv2.imshow( "Gaussian Filtering (sigma=0)", img2 )
cv2.imshow( "Gaussian Filtering (sigma=25)", img3 )
cv2.imshow( "Gaussian Filtering (sigma=50)", img4 )
cv2.waitKey( 0 )
cv2.destroyAllWindows()