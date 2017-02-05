#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import pylab as plt

img = cv2.imread("sample.jpg")
hist=img.ravel()
plt.hist(hist,256,[0,256])
plt.xlim([0,256])
plt.show()