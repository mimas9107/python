import numpy as np
import cv2

def image_quantization(f, bits):
    g = f.copy()
    levels = 2 ** bits
    interval = 256 / levels
    gray_level_interval = 255 / (levels - 1)
    
    # Create the lookup table
    table = np.zeros(256)
    for l in range(levels):
        table[int(l * interval):int((l + 1) * interval)] = round(l * gray_level_interval)
    
    # Apply the lookup table
    g = np.uint8(table[f])
    
    return g
	
	
def main( ):
    img1 = cv2.imread( "lenna.bmp", -1 )
    img2 = image_quantization( img1, 7 )
    img3 = image_quantization( img1, 5 )
    img4 = image_quantization( img1, 3 )
    img5 = image_quantization( img1, 1 )
    cv2.imshow( "Original Image", img1 )
    cv2.imshow( "Quantization (5-bit)", img2 )
    cv2.imshow( "Quantization (3-bit)", img3 )
    cv2.imshow( "Quantization (2-bit)", img4 )
    cv2.imshow( "Quantization (1-bit)", img5 )
    cv2.waitKey( 0 )
    cv2.destroyAllWindows()

main( )