import cv2

from picamera.array import PiRGBArray
from picamera import PiCamera
from detector import Detector
from calibration import Calibration

def capture_frames(camera):
  yield camera.stream()
  on_capture(camera.image())

if __name__ == '__main__':
  camera = PiCamera(resolution=(640, 480))
  rawCapture = PiRGBArray(camera)
  camera.capture(rawCapture, format="bgr")
  im = rawCapture.array
  #im = cv2.imread('photos/b1.jpg')
  #im = cv2.resize(im, (640, 480))

  detector = Detector()
  mushrooms = detector.detect(im) 
  cal = Calibration()

  for mushroom in mushrooms:
    (x, y, r) = mushroom
    print str(mushroom) + " " + str(cal.transform(x, y))
    cv2.circle(im, (x, y), r, (0, 255, 0), 2)
    cv2.circle(im, (x, y), 2, (0, 0, 255), 3)

  cv2.imshow("demo", im)
  cv2.waitKey()
