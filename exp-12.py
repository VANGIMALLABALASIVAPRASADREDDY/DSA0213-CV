import cv2
import numpy as np

img = cv2.imread("3.jpg", 0)
edges = cv2.Canny(img, 100, 200)
cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
