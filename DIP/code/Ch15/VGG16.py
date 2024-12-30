import numpy as np
import cv2
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions

model = VGG16( weights = "imagenet", include_top = True )
print( model.summary() )
img = cv2.imread( "Dog.jpg", -1 )
img = cv2.resize( img, ( 224, 224 ), interpolation = cv2.INTER_LINEAR )
x = image.img_to_array( img )
x = np.expand_dims( x, axis = 0 )
x = preprocess_input( x )
features = model.predict( x )
print( "Predicted:", decode_predictions( features, top = 3 )[0] )