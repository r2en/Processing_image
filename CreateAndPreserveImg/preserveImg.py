#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as numpy
import cv2

img = cv2.imread('../IMG/sample.png',cv2.IMREAD_GRAYSCALE)

cv2.imwrite('../IMG/grayscale.png',img)
cv2.imwrite('../IMG/grayscale.jpg',img)
