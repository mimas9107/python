import numpy as np
import cv2

img = cv2.imread( "Baboon.bmp", -1 )
nr1, nc1 = img.shape[:2]
nr2, nc2 = nr1 // 1, nc1 // 2
img1 = cv2.resize( img, ( nr2, nc2 ), interpolation = cv2.INTER_NEAREST ) # 縮小
img1 = cv2.resize( img1, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST ) # 放大

img2 = cv2.resize( img, ( nr2, nc2 ), interpolation = cv2.INTER_LINEAR )
img2 = cv2.resize( img2, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST )

img3 = cv2.resize( img, ( nr2, nc2 ), interpolation = cv2.INTER_CUBIC )
img3 = cv2.resize( img2, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST )

cv2.imshow( "Original Image", img )
cv2.imshow( "Nearest Neighbor", img1 )
cv2.imshow( "Bilinear", img2 )
cv2.imshow( "Bicubic", img3 )
cv2.waitKey( 0 )
cv2.destroyAllWindows()