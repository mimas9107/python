import numpy as np
import cv2
from cv2 import dnn

def get_class_list( ):
    with open( "synset_words.txt", "rt" ) as f:
        return [ x[x.find(" ") + 1:] for x in f ]

def main( ):
	img = cv2.imread( "Space_Shuttle.bmp", -1 )
	blob = dnn.blobFromImage( img, 1, ( 224, 224 ), False )
	network = dnn.readNetFromCaffe( "bvlc_googlenet.prototxt", 
		      "bvlc_googlenet.caffemodel" )
	network.setInput( blob )
	prob = network.forward( )
	classes = get_class_list( )
	print( "Best match:", classes[ prob.argmax( ) ] )
	cv2.imshow( "Input",  img )	
	cv2.waitKey( )

main( )