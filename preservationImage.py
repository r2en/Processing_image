#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as numpy
import cv2

img = cv2.imread('sample.png',cv2.IMREAD_GRAYSCALE)

cv2.imwrite('grayscale.png',img)
cv2.imwrite('grayscale.jpg',img)
