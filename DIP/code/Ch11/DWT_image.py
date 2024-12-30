import numpy as np
import cv2
import pywt

def DWT_image( f, wavelet ):
	nr, nc = f.shape[:2]
	coeffs = pywt.dwt2( f, wavelet )
	LL, (LH, HL, HH) = coeffs	
	
	nr1, nc1 = LL.shape[:2]
	g = np.zeros( [nr1 * 2, nc1 * 2], dtype = 'uint8' )

	# LL (Normalized for Display)
	LL_normalized = np.zeros( [nr1, nc1] )
	cv2.normalize( LL, LL_normalized, 0, 255, cv2.NORM_MINMAX )
	g[0:nr1,0:nc1] = np.uint8( LL_normalized[:,:] )
	
	# LH, HL, HH (Add 128 for Display)
	g[0:nr1,nc1:2*nc1] = np.uint8( np.clip( LH + 128, 0, 255 ) )
	g[nr1:2*nr1,0:nc1] = np.uint8( np.clip( HL + 128, 0, 255 ) )
	g[nr1:2*nr1,nc1:nc1*2] = np.uint8( np.clip( HH + 128, 0, 255 ) )	

	return g

def main( ):
	img1 = cv2.imread( "House.bmp", -1 )
	img2 = DWT_image( img1, 'db4' )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Discrete Wavelet Transform", img2 )
	cv2.waitKey( 0 )

main( )