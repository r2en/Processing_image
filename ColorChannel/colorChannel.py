#!/usr/bin/python
#-*- coding: utf-8 -*-

import numpy as np
import cv2

img = cv2.imread("sample.png")
RGB = cv2.split(img)
Blue = RGB[0]
Green = RGB[1]
Red = RGB[2]

images = ["Blue","Green","Red"]
color = [Blue,Green,Red]

for i in xrange(3):
	cv2.imshow(images[i],color[i])
	cv2.waitKey(0)
	cv2.destroyAllWindows()
