import numpy as np
import cv2

def image_formation_model( f, x0, y0, sigma ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	illumination = np.zeros( [ nr, nc ], dtype = 'float32' )
	for x in range( nr ):
		for y in range( nc ):
			illumination[x,y] = np.exp( -( ( x - x0 ) ** 2 + ( y - y0 ) ** 2 ) / 
 								( 2 * sigma * sigma ) )
	for x in range( nr ):
		for y in range( nc ):
			for k in range( 3 ):
				val = round( illumination[x,y] * f[x,y,k] )
				g[x,y,k] = np.uint8( val )
	return g
	
def main( ):
	img = cv2.imread( "../dataset/lena.ppm", -1 )
	nr, nc = img.shape[:2]
	x0 = nr // 2
	y0 = nc // 2
	sigma = 100
	img2 = image_formation_model( img, x0, y0, sigma )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Image Formation Model", img2 )
	cv2.waitKey( 0 )

main( )