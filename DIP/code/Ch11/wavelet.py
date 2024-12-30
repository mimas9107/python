import pywt
import matplotlib.pyplot as plt

# Haar Wavelet
plt.figure( 1 )
wavelet = pywt.Wavelet( 'db1' )
plt.stem( wavelet.filter_bank[0], use_line_collection = True )

# Daubechies Wavelet(4-Tap)
plt.figure( 2 )
wavelet = pywt.Wavelet( 'db2' )
plt.stem( wavelet.filter_bank[0], use_line_collection = True )

# Daubechies Wavelet(8-Tap)
plt.figure( 3 )
wavelet = pywt.Wavelet( 'db4' )
plt.stem( wavelet.filter_bank[0], use_line_collection = True )

plt.show( )