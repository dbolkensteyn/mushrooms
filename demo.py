import cv2
from detect import Detector

if __name__ == '__main__':
  im = cv2.imread("photos/b1.jpg")
  im = cv2.resize(im, (640, 480))

  detector = Detector()
  circles = detector.detect(im)

  for circle in circles:
    (x, y, r) = circle
    cv2.circle(im, (x, y), r, (0,255,0), 2)
    cv2.circle(im, (x, y), 2, (0,0,255), 3)

  cv2.imshow("demo", im)
  cv2.waitKey()
