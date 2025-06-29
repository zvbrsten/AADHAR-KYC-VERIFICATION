import cv2
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  

def detect_screen_or_print(image_pil):
    img = np.array(image_pil.convert("RGB"))
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Variance of Laplacian (focus)
    lap_var = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Color diversity: screens often have pixel-level color noise
    color_std = np.std(img)

    # Heuristic rules
    if lap_var < 100 or color_std > 75:
        return True, lap_var, color_std  # spoof
    return False, lap_var, color_std
