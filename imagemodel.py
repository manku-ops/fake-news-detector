import cv2
import numpy as np

def analyze_image(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    variance = np.var(gray)

    # Simple heuristic
    if variance < 500:
        return "Possibly manipulated image"
    else:
        return "Looks natural"
