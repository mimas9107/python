import numpy as np
import cv2

img1 = cv2.imread( "Building.bmp", -1 )
img2 = cv2.equalizeHist( cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) )
cv2.imshow( "Original Image", img1 )	
cv2.imshow( "Histogram Equalization", img2 )
cv2.waitKey( 0 )
cv2.destroyAllWindows()