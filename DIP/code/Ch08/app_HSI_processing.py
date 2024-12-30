import streamlit as st
import numpy as np
import cv2
from PIL import Image

# Function to convert RGB to HSI
def RGB_to_HSI(R, G, B):
    r = R / 255
    g = G / 255
    b = B / 255
    if R == G and G == B:
        H = -1.0
        S = 0.0
        I = (r + g + b) / 3
    else:
        x = (0.5 * ((r - g) + (r - b))) / np.sqrt((r - g) ** 2 + (r - b) * (g - b))
        if x < -1.0:
            x = -1.0
        if x > 1.0:
            x = 1.0
        theta = np.arccos(x) * 180 / np.pi
        if B <= G:
            H = theta
        else:
            H = 360.0 - theta
        S = 1.0 - 3.0 / (r + g + b) * min(r, g, b)
        I = (r + g + b) / 3
    return H, S, I

# Function to convert HSI to RGB
def HSI_to_RGB(H, S, I):
    if H == -1.0:
        r = I
        g = I
        b = I
    elif H >= 0 and H < 120:
        HH = H
        b = I * (1 - S)
        r = I * (1 + (S * np.cos(HH * np.pi / 180)) / np.cos((60 - HH) * np.pi / 180))
        g = 3.0 * I - (r + b)
    elif H >= 120 and H < 240:
        HH = H - 120.0
        r = I * (1 - S)
        g = I * (1 + (S * np.cos(HH * np.pi / 180)) / np.cos((60 - HH) * np.pi / 180))
        b = 3 * I - (r + g)
    else:
        HH = H - 240
        g = I * (1 - S)
        b = I * (1 + (S * np.cos(HH * np.pi / 180)) / np.cos((60 - HH) * np.pi / 180))
        r = 3 * I - (g + b)
    rr = round(r * 255)
    gg = round(g * 255)
    bb = round(b * 255)
    R = np.uint8(np.clip(rr, 0, 255))
    G = np.uint8(np.clip(gg, 0, 255))
    B = np.uint8(np.clip(bb, 0, 255))
    return R, G, B

# Function to process image based on HSI adjustments
def HSI_processing(f, angle=0, saturation=100, intensity=100):
    g = f.copy()
    nr, nc = f.shape[:2]
    for x in range(nr):
        for y in range(nc):
            H, S, I = RGB_to_HSI(f[x, y, 2], f[x, y, 1], f[x, y, 0])
            H = H + angle
            if H > 360:
                H = H - 360
            S = S * saturation / 100
            I = I * intensity / 100
            R, G, B = HSI_to_RGB(H, S, I)
            g[x, y, 0] = B
            g[x, y, 1] = G
            g[x, y, 2] = R
    return g

def main():
    st.title('HSI Image Processing')

    # Load the image
    img_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp"])
    if img_file is not None:
        image = Image.open(img_file)
        img = np.array(image)        
        # Check if the image is grayscale and convert it to RGB
        if len(img.shape) == 2 or img.shape[2] == 1:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        elif img.shape[2] == 4:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        
            
        # Initialize default values
        angle = st.sidebar.slider("Angle", min_value=0, max_value=360, value=0)
        saturation = st.sidebar.slider("Saturation (%)", min_value=0, max_value=200, value=100)
        intensity = st.sidebar.slider("Intensity (%)", min_value=0, max_value=200, value=100)

        # Process image based on sliders
        img_processed = HSI_processing(img, angle, saturation, intensity)

        # Display original and processed images
        st.image(img, caption='Original Image', use_column_width=True)
        st.image(img_processed, caption='Processed Image', use_column_width=True)

if __name__ == '__main__':
    main()
