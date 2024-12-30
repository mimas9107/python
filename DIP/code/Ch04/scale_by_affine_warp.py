'''
給予一張彩色影像nvidia.jpg及scale_by_affine_warp.py，請利用一對三組控制點方式，定義仿射轉換(affine transformation)方式，並放大或縮小影像。 
【提示】scale_by_affine_warp.py中，只需填寫問號的部分即可完成。
'''
import cv2
import numpy as np

# Load the image
image = cv2.imread( "nvidia.jpg", -1 )
if image is None:
    raise ValueError("Image not found or unable to load.")

# Get the dimensions of the image
(h, w) = image.shape[:2]

# Define the source points (control points on the original image)
# You can adjust these points as needed
src_points = np.float32([
    [w // 4, h // 4],
    [w * 3 // 4, h // 4],
    [w // 2, h * 3 // 4]
])


dst_points = np.float32([
    [?, ?], # 由您解答
    [?, ?], # 由您解答
    [?, ?], # 由您解答
])

# Compute the affine transformation matrix
M = cv2.getAffineTransform(src_points, dst_points)

# Apply the affine transformation
rotated_image = cv2.warpAffine(image, M, (w, h))

# Save or display the rotated image
cv2.imwrite('scaled_image.jpg', rotated_image)
# cv2.imshow('Rotated Image', rotated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
