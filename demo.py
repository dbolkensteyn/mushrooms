import cv2

from picamera.array import PiRGBArray
from picamera import PiCamera
from detector import Detector

def capture_frames(camera):
  yield camera.stream()
  on_capture(camera.image())

if __name__ == '__main__':
  camera = PiCamera(resolution=(640, 480))
  rawCapture = PiRGBArray(camera)

  camera.capture(rawCapture, format="bgr")
  im = rawCapture.array

  detector = Detector()
  mushrooms = detector.detect(im)

  mushroom = mushrooms.pop()
  cv2.circle(im, (x, y), r, (0, 255, 0), 2)
  cv2.circle(im, (x, y), 2, (0, 0, 255), 3)
  for other in mushrooms:
    (x, y, r) = circle
    cv2.circle(im, (x, y), r, (0, 255, 0), 2)
    cv2.circle(im, (x, y), 2, (0, 0, 255), 3)

  cv2.imshow("demo", im)
  cv2.waitKey()
