import numpy as np
import pywt

f = np.array( [ 14, 8, 6, 4, 3, 5, 9, 7 ] )

# Haar Wavelet
print( "Haar Wavelet" )
cA, cD = pywt.dwt( f, 'db1' )
print( "DWT Coefficients: ", cA, cD )
fp = pywt.idwt( cA, cD, 'db1' )
print( "Reconstruction: ", fp )

# Daubechies Wavelet (4-Tap)
print( "Daubechies Wavelet (4-Tap)" )
cA, cD = pywt.dwt( f, 'db2' )
print( "DWT Coefficients: ", cA, cD )
fp = pywt.idwt( cA, cD, 'db2' )
print( "Reconstruction: ", fp )

# Daubechies Wavelet (8-Tap)
print( "Daubechies Wavelet (8-Tap)" )
cA, cD = pywt.dwt( f, 'db4' )
print( "DWT Coefficients: ", cA, cD )
fp = pywt.idwt( cA, cD, 'db4' )
print( "Reconstruction: ", fp )