import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# 標準差
sigma = 1

# 高斯函數(2D)
X = np.linspace( -3 * sigma, 3 * sigma, 100 )
Y = np.linspace( -3 * sigma, 3 * sigma, 100 )
x, y = np.meshgrid( X, Y )
z = np.exp( -( x * x + y * y ) / ( 2 * sigma * sigma ) )

# 3D繪圖
fig = plt.figure( )
ax = plt.axes( projection = "3d" )
ax.plot_surface( x, y, z, cmap = cm.coolwarm, linewidth = 0, 
	             antialiased = False )
plt.xlabel( 'x' )
plt.ylabel( 'y' )
plt.show( )