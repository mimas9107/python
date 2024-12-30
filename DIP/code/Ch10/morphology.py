import numpy as np
import cv2

img1 = cv2.imread( "Bug.bmp", -1 )
print( "Morphological Image Processing" )
print( "(1) Erosion" )
print( "(2) Dilation" )
print( "(3) Opening" )
print( "(4) Closing" )
choice = eval( input( "Please enter your choice: " ) )
size = eval( input( "Size of structuring element: " ) )
kernel = np.ones( ( size, size ), np.uint8 )
if choice == 1:
	img2 = cv2.erode( img1, kernel, iterations = 1 )
elif choice == 2:
	img2 = cv2.dilate( img1, kernel, iterations = 1 )
elif choice == 3:
	img2 = cv2.morphologyEx( img1, cv2.MORPH_OPEN, kernel )
else:
	img2 = cv2.morphologyEx( img1, cv2.MORPH_CLOSE, kernel )
cv2.imshow( "Original Image",  img1 )	
cv2.imshow( "Morphological Image Processing", img2 )
cv2.waitKey( 0 )