import numpy as np
import cv2

img1 = cv2.imread( "Brunch.bmp", -1 )
img2 = cv2.stylization( img1 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Stylization", img2 )
cv2.waitKey( 0 )