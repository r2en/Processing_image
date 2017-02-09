#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import pylab as plt

cups = cv2.imread('cups.jpg')
 
cups_preprocessed  = cv2.cvtColor(cv2.GaussianBlur(cups, (7,7), 0), cv2.COLOR_BGR2GRAY)
 
_, cups_thresh = cv2.threshold(cups_preprocessed, 200, 255, cv2.THRESH_BINARY)

cups_edges = cv2.Canny(cups_preprocessed,threshold1=90,threshold2=110)

circles = cv2.HoughCircles(cups_edges, cv2.cv.CV_HOUGH_GRADIENT, dp=1.5, minDist=50, minRadius=20, maxRadius=130)
cups_circles = np.copy(cups)

if circles is not None and len(circles) > 0:

    circles = circles[0]
    for (x, y, r) in circles:
        x, y, r = int(x), int(y), int(r)
        cv2.circle(cups_circles, (x, y), r, (255, 255, 0), 4)
	plt.imshow(cv2.cvtColor(cups_circles, cv2.COLOR_BGR2RGB))
 
print('number of circles detected: %d' % len(circles[0]))

cv2.imshow('cups',cups_circles)
cv2.waitKey(0)
cv2.destroyAllWindows()

