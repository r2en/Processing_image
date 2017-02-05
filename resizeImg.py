#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as numpy
import cv2

img = cv2.imread("sample.png",cv2.IMREAD_COLOR)

orgHeight,orgWidth, = img.shape[:2]
size = (orgHeight/2,orgWidth/2)

halfImg = cv2.resize(img,size)
twiceImg = cv2.resize(img,None,fx = 2,fy = 2)

cv2.imwrite("half.jpg",halfImg)
cv2.imwrite("twiceImg.jpg",twiceImg)

