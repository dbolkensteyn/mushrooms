import cv2
import numpy as np

def auto_canny(image, sigma=0.33):
  # compute the median of the single channel pixel intensities
  v = np.median(image)
 
  # apply automatic Canny edge detection using the computed median
  lower = int(max(0, (1.0 - sigma) * v))
  upper = int(min(255, (1.0 + sigma) * v))
  edged = cv2.Canny(image, lower, upper)
 
  # return the edged image
  return edged

im = cv2.imread("photos/b1.jpg")
im = cv2.resize(im, (640, 480))
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
_, im = cv2.threshold(im, 130, 255, cv2.THRESH_BINARY)
im = cv2.erode(im, (3, 3))
im = auto_canny(im)

cv2.imshow("demo", im)
cv2.waitKey()
