import numpy as np
import cv2

def HSV_histogram_equalization( f ):
	hsv = cv2.cvtColor( f, cv2.COLOR_BGR2HSV )
	hsv[:,:,2] = cv2.equalizeHist( hsv[:,:,2] )
	g = cv2.cvtColor( hsv, cv2.COLOR_HSV2BGR )
	return g

def YCbCr_histogram_equalization( f ):
    ycrcb = cv2.cvtColor( f, cv2.COLOR_BGR2YCrCb )
    ycrcb[:,:,0] = cv2.equalizeHist( ycrcb[:,:,0] )
    g = cv2.cvtColor( ycrcb, cv2.COLOR_YCrCb2BGR )
    return g

def RGB_histogram_equalization( f ):
    g = f.copy()
    for i in range(3):
        g[:,:,i] = cv2.equalizeHist( f[:,:,i] )
    return g

def main( ):
    img1 = cv2.imread( "Rose.bmp", -1 )
    img2_hsv = HSV_histogram_equalization( img1 )
    img2_ycbcr = YCbCr_histogram_equalization( img1 )
    img2_rgb = RGB_histogram_equalization( img1 )
    cv2.imshow( "Original Image", img1 )	
    cv2.imshow( "Histogram Equalization(HSV)", img2_hsv )
    cv2.imshow( "Histogram Equalization(YCbCr)", img2_ycbcr )
    cv2.imshow( "Histogram Equalization(RGB)", img2_rgb )
    cv2.waitKey( 0 )
    cv2.destroyAllWindows()

main( )