import numpy as np
import cv2

def entropy( f ):
	nr, nc = f.shape[:2]
	pdf = np.zeros( 256 )
	for x in range( nr ):
		for y in range( nc ):
			pdf[f[x,y]] += 1
	pdf /= ( nr * nc )
	H = 0
	for k in range( 256 ):
		if pdf[k] != 0:
			H += ( -pdf[k] * np.log2( pdf[k] ) )
	return H

def main( ):
	img = cv2.imread( "Lenna.bmp", -1 )
	H = entropy( img )
	print( "Entropy =", H )

main( )