#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import pylab as plt

img = cv2.imread('sample.png',flags=0)

if img is None:
	print ("None")
	exit()
plt.imshow(img)
plt.show()