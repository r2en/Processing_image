#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as numpy
import cv2

img = cv2.imread('sample.png')

# coordinate
blue = img.item(10,20,0)
green = img.item(10,20,1)
red = img.item(10,20,2)

print 'blue = ' + str(blue)
print 'green = ' + str(green)
print 'red = ' + str(red)

print type(blue)