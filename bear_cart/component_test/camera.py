#!/usr/bin/python3

import sys
import cv2

from picamera2 import Picamera2

# Grab images as numpy arrays and leave everything else to OpenCV.

cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'RGB888', "size": (640, 480)}))
picam2.start()

while True:
    im = picam2.capture_array()
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Camera", im)
    # Press "q" to quit
    if cv2.waitKey(1)==ord('q'):
        cv2.destroyAllWindows()
        sys.exit()