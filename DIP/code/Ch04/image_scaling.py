import numpy as np
import cv2

img1 = cv2.imread( "Lenna.bmp", -1 )
nr, nc = img1.shape[:2]
row_scale = eval( input( "Please enter scale for row: " ) )
col_scale = eval( input( "Please enter scale for col: " ) )
nr2 = int( nr * row_scale  )
nc2 = int( nc * col_scale  )
img2 = cv2.resize( img1, ( nr2, nc2 ), interpolation = cv2.INTER_NEAREST )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Image Scaling", img2 )
cv2.waitKey( 0 )

cv2.destroyAllWindows()