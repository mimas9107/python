import numpy as np
import matplotlib.pyplot as plt

# 標準差
sigma = 1

# 高斯函數
x = np.linspace( -3 * sigma, 3 * sigma, 100 )
g = np.exp( -( x * x ) / ( 2 * sigma * sigma ) )
# 高斯函數的一階導函數
gx = -( x / ( sigma * sigma ) ) * g
# 高斯函數的二階導函數
gxx = ( ( x * x - sigma * sigma ) / pow( sigma, 4 ) ) * g

# 繪圖
plt.figure( 1 )
plt.plot( x, g )
plt.xlabel( "x" )
plt.ylabel( "g(x)" )
plt.figure( 2 )
plt.plot( x, gx )
plt.xlabel( "x" )
plt.ylabel( "g'(x)" )
plt.figure( 3 )
plt.plot( x, gxx )
plt.xlabel( "x" )
plt.ylabel( "g''(x)" )
plt.show( )