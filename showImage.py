#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as numpy
import cv2

#cv2.IMREAD_UNCHANGED
#cv2.IMREAD_COLOR
img = cv2.imread('sample.png', cv2.IMREAD_GRAYSCALE)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()