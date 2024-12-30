import numpy as np
import cv2

img1 = cv2.imread( "Gallery.bmp", -1 )
nr, nc = img1.shape[:2]
pts1 = np.float32( [ [ 795, 350 ], [ 795, 690 ], [ 1090, 720 ], [ 1090, 250 ] ] )
pts2 = np.float32( [ [ 0, 0 ], [ 0, 500 ], [ 650, 500 ], [ 650, 0 ] ] )
T = cv2.getPerspectiveTransform( pts1, pts2 )
img2 = cv2.warpPerspective( img1, T, ( 650, 500 ) )

pts1 = pts1.astype(np.int32)
cv2.polylines( img1, [pts1], True, ( 255, 0, 0 ), 4)
pts2 = pts2.astype(np.int32)
cv2.polylines( img1, [pts2], True, ( 0, 255, 0 ), 4)

cv2.imshow( "Original Image", img1 )
cv2.imshow( "Perspective Transform", img2 )
cv2.waitKey( 0 )
cv2.destroyAllWindows()