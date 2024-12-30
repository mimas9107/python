import cv2
import numpy as np
import scipy.special as special
import matplotlib.pyplot as plt

def histogram( f ):
    plt.clf()
    if f.ndim != 3:
        hist = cv2.calcHist( [f], [0], None, [256], [0,256] )
        plt.plot( hist )
    else:
        color = ( 'b', 'g', 'r' )
        for i, col in enumerate( color ):
            hist = cv2.calcHist( f, [i], None, [256], [0,256] )
            plt.plot( hist, color = col )
    plt.xlim( [0,256] )
    plt.xlabel( "Intensity" )
    plt.ylabel( "#Intensities" )
    plt.pause(0.001)


def beta_correction(f, a=2.0, b=2.0):
    # Create the lookup table
    x = np.linspace(0, 1, 256)
    table = np.round(special.betainc(a, b, x) * 255).astype(np.uint8)
    
    # Apply the lookup table to the image
    g = table[f]
    
    return g

# Initialize the webcam
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
    
beta_enabled = False

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting...")
        break

    if beta_enabled:    
        # Convert the image from BGR to YCrCb color space
        ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        
        # Split the channels
        y, cr, cb = cv2.split(ycrcb)
        
        # Equalize the histogram of the Y channel
        y_eq = cv2.equalizeHist(y)
        
        # Merge the equalized Y channel back with the Cr and Cb channels
        ycrcb_eq = cv2.merge([y_eq, cr, cb])
        
        # Convert the image back to BGR color space
        frame = cv2.cvtColor(ycrcb_eq, cv2.COLOR_YCrCb2BGR)

    histogram(frame)

    # Display the resulting frame
    cv2.imshow('Webcam', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('b'):
        beta_enabled = not beta_enabled

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
