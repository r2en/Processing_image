#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as numpy
import cv2

img = cv2.imread('sample.png')

# coordinate
pixelValue = img[10,20]

print 'pixelValue = ' + str(pixelValue)

print type(img)
print type(pixelValue)