import numpy as np
import cv2

def Sobel_gradient(f, direction=1):
    # Sobel kernels
    sobel_y = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]])
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    
    if direction == 1:  # Horizontal gradients
        grad_x = cv2.filter2D(f, cv2.CV_32F, sobel_x)
        gx = abs(grad_x)
        g = np.uint8(np.clip(gx, 0, 255))
    elif direction == 2:  # Vertical gradients
        grad_y = cv2.filter2D(f, cv2.CV_32F, sobel_y)
        gy = abs(grad_y)
        g = np.uint8(np.clip(gy, 0, 255))
    else:  # Magnitude of gradients
        grad_x = cv2.filter2D(f, cv2.CV_32F, sobel_x)
        grad_y = cv2.filter2D(f, cv2.CV_32F, sobel_y)
        magnitude = np.sqrt(grad_x**2 + grad_y**2)
        g = np.uint8(np.clip(magnitude, 0, 255))
    return g

def visualize_gradient_direction(img, grad_x, grad_y):
    h, w = img.shape[:2]
    vis_img = img.copy()
    
    # Parameters for arrow visualization
    step = 16  # Distance between arrows
    scale = 0.1  # Scale for arrow length

    for y in range(0, h, step):
        for x in range(0, w, step):
            gx = grad_x[y, x]
            gy = grad_y[y, x]
            
            if gx == 0 and gy == 0:
                continue
            
            angle = np.arctan2(gy, gx)
            magnitude = np.sqrt(gx**2 + gy**2)

            # Determine the endpoint of the arrow
            end_x = int(x + scale * magnitude * np.cos(angle))
            end_y = int(y + scale * magnitude * np.sin(angle))
            
            # Draw arrow
            cv2.arrowedLine(vis_img, (x, y), (end_x, end_y), (128, 128, 128), 1, tipLength=0.3)
    
    return vis_img

def main():
    img = cv2.imread("Lenna.bmp", cv2.IMREAD_GRAYSCALE)
    grad_x = Sobel_gradient(img, 1)
    grad_y = Sobel_gradient(img, 2)
    g = Sobel_gradient(img, 3)
    
    vis_img = visualize_gradient_direction(img, grad_x, grad_y)
    
    cv2.imshow("Original Image", img)
    cv2.imshow("Gradient in x", grad_x)
    cv2.imshow("Gradient in y", grad_y)
    cv2.imshow("Gradient", g)
    cv2.imshow("Gradient Direction", vis_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()
