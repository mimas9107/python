import numpy as np
import cv2

def jpeg_compression( f, percentage = 25 ):
	normalize = np.array( [ [ 16, 11, 10, 16,  24,  40,  51,  61 ],
						    [ 12, 12, 14, 19,  26,  58,  60,  55 ],
						    [ 14, 13, 16, 24,  40,  57,  69,  56 ],
						    [ 14, 17, 22, 29,  51,  87,  80,  62 ],
						    [ 18, 22, 37, 56,  68, 109, 103,  77 ],
						    [ 24, 35, 55, 64,  81, 104, 113,  92 ],
						    [ 49, 64, 78, 87, 103, 121, 120, 101 ],
						    [ 72, 92, 95, 98, 112, 100, 103,  99 ] ] )
	table = np.array( [ [  0,  1,  5,  6, 14, 15, 27, 28 ],
					    [  2,  4,  7, 13, 16, 26, 29, 42 ],
					    [  3,  8, 12, 17, 25, 30, 41, 43 ],
					    [  9, 11, 18, 24, 31, 40, 44, 53 ],
					    [ 10, 19, 23, 32, 39, 45, 52, 54 ],
					    [ 20, 22, 33, 38, 46, 51, 55, 60 ],
					    [ 21, 34, 37, 47, 50, 56, 59, 61 ],
					    [ 35, 36, 48, 49, 57, 58, 62, 63 ] ] )
	g = f.copy( )
	nr, nc = f.shape[:2]
	n = 8
	coeffs = np.zeros( [ 8, 8 ] )
	for x in range( 0, nr, n ):
		for y in range( 0, nc, n ):
			# Define 8 x 8 Blocks
			for k in range( n ):
				for l in range( n ):
					if x + k < nr and y + l < nc:
						coeffs[k,l] = int( f[x+k,y+l] )
					else:
						coeffs[k,l] = 0
			# JPEG Compression
			coeffs = coeffs - 128
			coeffs = cv2.dct( np.float32( coeffs ) )  
			coeffs = np.round( coeffs )
			coeffs = np.round( coeffs / normalize )	
			# Thresholding
			thresh = n * n * percentage / 100
			for k in range( n ):
				for l in range( n ):
					if table[k,l] > thresh - 1:
						coeffs[k,l] = 0
			# JPEG Decompression
			coeffs = coeffs * normalize
			coeffs = cv2.idct( np.float32( coeffs ) )
			coeffs = np.round( coeffs )
			coeffs = coeffs + 128			
			# Reconstruction
			for k in range( n ):
				for l in range( n ):
					if x + k < nr and y + l < nc:
						value = np.clip( coeffs[k,l], 0, 255 )
						g[x+k,y+l] = np.uint8( value )
					else:
						g[x,y] = 0	
	return g

def main( ):
	img1 = cv2.imread( "House.bmp", -1 )
	img2 = jpeg_compression( img1, 30 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Compressed Image", img2 )
	cv2.waitKey( 0 )

main( )