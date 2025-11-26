# Random OpenCV File
import cv2
import numpy as np
img = np.random.randint(0, 255, (200,200,3), dtype=np.uint8)
blur = cv2.GaussianBlur(img, (5,5), 0)
edges = cv2.Canny(blur, 50, 150)
print('Edges shape:', edges.shape)
