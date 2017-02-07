#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as numpy
import pylab as plt
import cv2

img = cv2.imread("sample.png",cv2.IMREAD_COLOR)

orgHeight,orgWidth, = img.shape[:2]
print orgHeight
print orgWidth
size = (orgHeight/2,orgWidth/2)
print size

half = cv2.resize(img,size)
twice = cv2.resize(img,None,fx = 2,fy = 2)

cv2.imshow("half",half)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("twice",twice)
cv2.waitKey(0)
cv2.destroyAllWindows()
