# OpenCV Script
import cv2, numpy as np
img = np.random.randint(0,255,(200,200,3),dtype=np.uint8)
edges = cv2.Canny(img, 100, 200)
