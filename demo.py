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

  cv2.imshow("demo", im)
  cv2.waitKey()
