import numpy as np

z = np.array( [ 1, 2, 3, 4, 1, 2 ] )
z_exp = np.exp( z )
sum = np.sum( z_exp )
softmax = np.round( z_exp / sum, 3 )
print( softmax )