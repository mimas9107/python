import numpy as np
import cv2

img = cv2.imread( "../dataset/mature_girl.jpg", -1 )
img1, img2 = cv2.pencilSketch( img )
cv2.imshow( "Original Image", img )
cv2.imshow( "Pencil Sketch 1", img1 )
cv2.imshow( "Pencil Sketch 2", img2 )
cv2.waitKey( 0 )

cv2.destroyAllWindows()