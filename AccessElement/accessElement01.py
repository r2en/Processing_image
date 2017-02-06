#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as numpy
import cv2

img = cv2.imread('sample.png')

print 'ndim is ' + str(img.ndim)
print 'shape is ' + str(img.shape)
print 'size is ' + str(img.size)
print 'dtype is ' + str(img.dtype)