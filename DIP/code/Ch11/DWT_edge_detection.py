import numpy as np
import cv2
import pywt

def DWT_edge_detection( f, wavelet ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	coeffs = pywt.dwt2( f, wavelet )
	LL, (LH, HL, HH) = coeffs	
	LL.fill( 0 )
	coeffs = LL, (LH, HL, HH)
	output = pywt.idwt2( coeffs, wavelet ) 
	gradients = np.uint8( np.clip( abs( output ), 0, 255 ) )
	thresh, g = cv2.threshold( gradients, 127, 255, cv2.THRESH_OTSU )
	return g

def main( ):
	img1 = cv2.imread( "House.bmp", -1 )
	img2 = DWT_edge_detection( img1, 'db8' )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Edge Detection using DWT", img2 )
	cv2.waitKey( 0 )

main( )