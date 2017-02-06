#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import pylab as plt

img = cv2.imread("../IMG/sample.png")

hist = cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(hist)
plt.xlim([0,256])
plt.show()
