#Read an image

import numpy as np
import cv2
import time

img=cv2.imread("image.jpg")
img=cv2.imwrite("image.png",img)
cv2.imshow("original",img)
time.sleep(5)
cv2.destroyAllWindows()
