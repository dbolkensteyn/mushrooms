import cv2

from camera import Camera
from detector import Detector

def on_capture(im):
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

def capture_frame(camera, controller):
  yield camera.stream()
  on_capture(camera.image())

if __name__ == '__main__':
  camera = Camera(20)
  camera.capture_sequence(capture_frames(camera))
