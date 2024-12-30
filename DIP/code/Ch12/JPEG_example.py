import numpy as np
import cv2

normalize = np.array( [ [ 16, 11, 10, 16,  24,  40,  51,  61 ],
						[ 12, 12, 14, 19,  26,  58,  60,  55 ],
						[ 14, 13, 16, 24,  40,  57,  69,  56 ],
						[ 14, 17, 22, 29,  51,  87,  80,  62 ],
						[ 18, 22, 37, 56,  68, 109, 103,  77 ],
						[ 24, 35, 55, 64,  81, 104, 113,  92 ],
						[ 49, 64, 78, 87, 103, 121, 120, 101 ],
						[ 72, 92, 95, 98, 112, 100, 103,  99 ] ] )

img = cv2.imread( "Lenna.bmp", -1 )
block  = img[260:268,260:268]
print( "Original Block" )
print( block )

# JPEG Forward Transform
coeffs = np.array( [8, 8], dtype = 'int' )
coeffs = block.astype('int' ) - 128
print( "Minus 128" )
print( coeffs )

coeffs = np.round( cv2.dct( np.float32( coeffs ) ) )
print( "Forward DCT" )
print( coeffs )  

coeffs = np.round( coeffs / normalize )
print( "Normalization" )
print( coeffs ) 

print( "-" * 60 )

# JPEG Inverse Transform
coeffs = coeffs * normalize
print( "Denormalization" )
print( coeffs ) 

coeffs = np.round( cv2.idct( coeffs ) )
print( "Inverse DCT" )
print( coeffs )

coeffs = np.round( coeffs + 128 )
print( "Plus 128 (Reconstruction)" )
print( coeffs )