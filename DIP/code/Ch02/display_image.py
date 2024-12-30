import numpy as np
import cv2

img1 = cv2.imread( "breakfast.bmp", -1 )
x = 450
y = 100
w = 256
h = 256


roi = img1[y:y+h, x:x+w, :].copy()

img1_r = np.zeros_like(roi)
img1_g = np.zeros_like(roi)
img1_b = np.zeros_like(roi)

img1_r [:, :, 2] = roi[:, :, 2]
img1_g [:, :, 1] = roi[:, :, 1]
img1_b [:, :, 0] = roi[:, :, 0]

cv2.rectangle(img1, (x, y), (x+w, y+h), (255, 0, 0), 3)
text = 'Latte'
fontFace = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img1, text, (x-5, y-5), fontFace, 2.0, color=(255, 0, 0), thickness=2)


cv2.imshow('original image', img1)
# cv2.imshow('red-channel image', img1_r)
# cv2.imshow('green-channel image', img1_g)
# cv2.imshow('blue-channel image', img1_b)
uppder_img = np.concatenate((roi, img1_r), axis=1)
lower_img = np.concatenate((img1_g, img1_b), axis=1)
merged_img = np.concatenate((uppder_img, lower_img), axis=0)
cv2.imshow('merged image', merged_img)
cv2.waitKey( 0 )
cv2.destroyAllWindows( )
