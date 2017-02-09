#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import pylab as plt

cups = cv2.imread('cups.jpg')
 
cups_preprocessed  = cv2.cvtColor(cv2.GaussianBlur(cups, (7,7), 0), cv2.COLOR_BGR2GRAY)
 
_, cups_thresh = cv2.threshold(cups_preprocessed, 200, 255, cv2.THRESH_BINARY)

cups_edges = cv2.Canny(cups_preprocessed,threshold1=90,threshold2=110)
plt.imshow(cv2.cvtColor(cups_edges,cv2.COLOR_GRAY2RGB))
cv2.imshow('cups',cups_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()