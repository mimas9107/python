import numpy as np
from scipy.signal import convolve2d

x = np.array( [ [ 1,  2,  3,  4,  5],
                [ 6,  7,  8,  9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],] )

# 濾波器
h = np.array( [ [0, 0, 0],
                [0, 0, 0],
                [0, 0, 1] ] )

y = convolve2d( x, h, 'same' )
print( "x =" )
print( x )
print( "h =" )
print( h )
print( "Convolution y =" )
print( y )