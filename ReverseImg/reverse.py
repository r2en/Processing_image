#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as numpy
import cv2

img = cv2.imread("../IMG/sample.png",cv2.IMREAD_COLOR)

xAxis = cv2.flip(img,0)
yAxis = cv2.flip(img,1)
xyAxis = cv2.flip(img, -1)

cv2.imwrite('../IMG/xAxis.jpg',xAxis)
cv2.imwrite('../IMG/yAxis.jpg',yAxis)
cv2.imwrite('../IMG/xyAxis.jpg', xyAxis)
