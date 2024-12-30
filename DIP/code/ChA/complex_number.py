import numpy as np

z = 3 + 4j							
magnitude = abs( z )				
theta = np.degrees( np.angle( z ) )
print( "z =", z )
print( "Magnitude =", magnitude )
print( "Phase Angle =", theta )