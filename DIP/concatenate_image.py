import numpy as np
import cv2

def draw_bbox(img, pt1, pt2, label, color=(255, 0, 0)):
    fontFace = cv2.FONT_HERSHEY_PLAIN
    cv2.rectangle(img, pt1, pt2, color, 2)
    cv2.putText(img, label, (pt1[0]-5, pt1[1]-5), fontFace, 2.0, color=(255, 0, 0), thickness=2)

img1 = cv2.imread( "breakfast.bmp", -1 )
# Assign ROI's coordinates
x = 450
y = 100
w = 256
h = 256

# Extract ROI from the image
roi = img1[y:y+h, x:x+w, :]

# Separate each channel image from an RGB image
img1_r = np.zeros_like(roi)
img1_g = np.zeros_like(roi)
img1_b = np.zeros_like(roi)
img1_r [:, :, 2] = roi[:, :, 2]
img1_g [:, :, 1] = roi[:, :, 1]
img1_b [:, :, 0] = roi[:, :, 0]

# Concatenate horizontally
upper_img = np.concatenate((roi, img1_r), axis=1)
# Concatenate horizontally
lower_img = np.concatenate((img1_g, img1_b), axis=1)
# Concatenate vertically
merged_img = np.concatenate((upper_img, lower_img), axis=0)

# Draw bbox (i.e., bounding box)
draw_bbox(img1, (x, y), (x+w, y+h), 'Latte')

# Call cv2.imshow to display images
cv2.imshow('original image', img1)
cv2.imshow('merged image', merged_img)

cv2.waitKey( 0 )
cv2.destroyAllWindows( )

cv2.imwrite('breakfast_labeled.bmp', img1)
cv2.imwrite('roi_merged.bmp', merged_img)