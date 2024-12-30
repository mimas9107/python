import numpy as np
import cv2
import pywt

def DWT_enhancement( f, method, wavelet ):
	nr, nc = f.shape[:2]
	coeffs = pywt.dwt2( f, wavelet )
	LL, (LH, HL, HH) = coeffs	
	if method == 1:  # LL only
		LH.fill( 0 )
		HL.fill( 0 )
		HH.fill( 0 )	
	elif method == 2: # LH only
		LL.fill( 0 )
		HL.fill( 0 )
		HH.fill( 0 )
	elif method == 3: # HL only
		LL.fill( 0 )
		LH.fill( 0 )
		HH.fill( 0 )
	elif method == 4: # HH only
		LL.fill( 0 )
		LH.fill( 0 )
		HL.fill( 0 )	
	coeffs = LL, (LH, HL, HH)
	output = pywt.idwt2( coeffs, wavelet ) 
	g = f.copy( )
	if method == 1:
		g = np.uint8( np.clip( output, 0, 255 ) )
	else:
		temp = np.zeros( [ nr, nc ] )
		cv2.normalize( output, temp, 0, 255, cv2.NORM_MINMAX )
		g = np.uint8( temp )
	return g

def main( ):
	print( "Image Enhancement using DWT:" )
	print( "(1) LL only" )
	print( "(2) LH only" )
	print( "(3) HL only" )
	print( "(4) HH only" )
	method = eval( input( "Please enter your choice: " ) )
	img1 = cv2.imread( "House.bmp", -1 )
	img2 = DWT_enhancement( img1, method, 'db1' )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Image Enhancement using DWT", img2 )
	cv2.waitKey( 0 )

main( )