import cv2
import numpy as np

class Detector:
  def auto_canny(self, image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
   
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
   
    # return the edged image
    return edged

  def detect(self, im):
    gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret = cv2.threshold(im, 130, 255, cv2.THRESH_BINARY)
    gray_im = ret[1]
    gray_im = cv2.erode(gray_im, (3, 3))
    gray_im = self.auto_canny(gray_im)

    roi = (82, 128, 495, 400)

    circles = cv2.HoughCircles(gray_im, cv2.cv.CV_HOUGH_GRADIENT, 1, minDist=10, param1=50, param2=13, minRadius=7, maxRadius=18)
    result = []
    if circles is not None:
      circles = np.uint16(np.around(circles))
      for i in circles[0,:]:
          x, y, r = i

          if x >= roi[0] and x <= roi[2] and y >= roi[1] and y <= roi[3]:
            result.append([x, y, r])

    return result
