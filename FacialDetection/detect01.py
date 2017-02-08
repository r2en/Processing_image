#!/usr/bin/python
#-*- coding: utf-8 -*-

import numpy as np
import cv2

cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"

image_path = "lena.jpg"
color = (255, 255, 255)

image = cv2.imread(image_path)
image_gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)

cascade = cv2.CascadeClassifier(cascade_path)
facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

print "face rectangle"
print facerect

if len(facerect) > 0:
    for rect in facerect:
        cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

    cv2.imshow("detected.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
