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
gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
_, gray_im = cv2.threshold(im, 130, 255, cv2.THRESH_BINARY)
gray_im = cv2.erode(gray_im, (3, 3))
gray_im = auto_canny(gray_im)

circles = cv2.HoughCircles(gray_im, cv2.cv.CV_HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=10, maxRadius=100)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(im, (i[0],i[1]), i[2], (0,255,0), 2)
    # draw the center of the circle
    cv2.circle(im, (i[0],i[1]), 2, (0,0,255), 3)

cv2.imshow("demo", im)
cv2.waitKey()
