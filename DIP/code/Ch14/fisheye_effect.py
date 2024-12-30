import numpy as np
import cv2

def fisheye_effect( f, scale=1.0):
    nr, nc = f.shape[:2]
    map_x = np.zeros( [nr, nc], dtype = 'float32' )
    map_y = np.zeros( [nr, nc], dtype = 'float32' )
    x0, y0 = nr // 2, nc // 2
    R = np.sqrt( nr ** 2 + nc ** 2 ) / 2
    R = R * scale
    for x in range( nr ):
        for y in range( nc ):
            r = np.sqrt( ( x - x0 ) ** 2 + ( y - y0 ) ** 2 )
            if r == 0:  theta = 0
            else:		theta = np.arccos( ( x - x0 ) / r )
            r = ( r * r ) / R
            if y - y0 < 0:  theta = -theta
            map_x[x,y] = np.clip( y0 + r * np.sin( theta ), 0, nc - 1 )
            map_y[x,y] = np.clip( x0 + r * np.cos( theta ), 0, nr - 1 )
    g = cv2.remap( f, map_x, map_y, cv2.INTER_CUBIC )
    return g

def main( ):
    img1 = cv2.imread("../dataset/mature_girl.jpg", -1)    
    cv2.imshow( "Original Image", img1 )
    for s in [0.5, 1, 1.5]:
        img2 = fisheye_effect( img1 , scale=s)
        cv2.imwrite(f'mature_girl_fished_{s}.bmp', img2)
    cv2.destroyAllWindows()

main( )