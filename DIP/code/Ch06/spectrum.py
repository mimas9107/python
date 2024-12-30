import numpy as np
import cv2
from numpy.fft import fft2, fftshift

def spectrum( f ):
	F = fft2( f )
	Fshift = fftshift( F )
	mag = 20 * np.log( np.abs( Fshift ) + 1 )
	mag = mag / mag.max( ) * 255.0
	g = np.uint8( mag )
	return g

def phase_spectrum( f ):
	F = fft2( f )
	phase = np.angle( F, deg = True )
	nr, nc = phase.shape[:2]
	for x in range( nr ):
		for y in range( nc ):
			if phase[x,y] < 0:
				phase[x,y] = phase[x,y] + 360
			phase[x,y] = int( phase[x,y] * 255 / 360 )
	g = np.uint8( np.clip( phase, 0, 255 ) )
	return g
	
def main( ):
	img = cv2.imread( "Lenna.bmp", -1 )
	magnitude = spectrum( img )
	phase = phase_spectrum( img )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Frequency Spectrum", magnitude )
	cv2.imshow( "Phase Specrum", phase )
	cv2.waitKey( 0 )

main( )