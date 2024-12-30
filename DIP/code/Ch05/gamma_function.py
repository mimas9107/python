import numpy as np
import matplotlib.pyplot as plt

gamma1 = 0.1
gamma2 = 0.2
gamma3 = 0.5
gamma4 = 1.0
gamma5 = 2.0
gamma6 = 5.0
gamma7 = 10.0

c1 = 255.0 / ( 255.0 ** gamma1 )
c2 = 255.0 / ( 255.0 ** gamma2 )
c3 = 255.0 / ( 255.0 ** gamma3 )
c4 = 255.0 / ( 255.0 ** gamma4 )
c5 = 255.0 / ( 255.0 ** gamma5 )
c6 = 255.0 / ( 255.0 ** gamma6 )
c7 = 255.0 / ( 255.0 ** gamma7 )

x  = np.linspace( 0, 255, 100 )

y1 = x ** gamma1 * c1
y2 = x ** gamma2 * c2
y3 = x ** gamma3 * c3
y4 = x ** gamma4 * c4
y5 = x ** gamma5 * c5
y6 = x ** gamma6 * c6
y7 = x ** gamma7 * c7

plt.plot( x, y1, label=f'gamma={gamma1}')
plt.plot( x, y2, label=f'gamma={gamma2}')
plt.plot( x, y3, label=f'gamma={gamma3}')
plt.plot( x, y4, label=f'gamma={gamma4}')
plt.plot( x, y5, label=f'gamma={gamma5}')
plt.plot( x, y6, label=f'gamma={gamma6}')

plt.ylabel( "Output Intensity" )
plt.xlabel( "Input Intensity" )
plt.xlim( [0,255] )
plt.ylim( [0,255] )
plt.legend( loc = 'lower right' )

plt.show( )