#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as numpy
import cv2

img = cv2.imread('sample.png')

print type(img)

pixelValue = img[10,20]
print type(pixelValue)
print 'pixelValue = ' + str(pixelValue)

blue = img[10,20,0]
green = img[10,20,1]
red = img[10,20,2]

print type(blue)
print 'blue = ' + str(blue)
print 'green = ' + str(green)
print 'red = ' + str(red)

blue = img.item(10,20,0)
green = img.item(10,20,1)
red = img.item(10,20,2)

print type(blue)
print 'blue = ' + str(blue)
print 'green = ' + str(green)
print 'red = ' + str(red)

img[10,20,0] = 100
print img[10,20,0]






