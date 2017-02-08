#!/usr/bin/python
#-*- coding: utf-8 -*-

import cv2
import pylab as plt
import numpy as np

im = cv2.imread("sample.png")

if im.ndim == 2:
	plt.hist(im.flatten(),256,range=(0,255),fc='k')
	plt.show()

elif im.ndim == 3:

	plt.subplot(311)
	plt.hist(im[:,:,0].flatten(),256,range=(0,255),fc='b')
	plt.subplot(312)
	plt.hist(im[:,:,1].flatten(),256,range=(0,255),fc='g')
	plt.xlim(0,255)
	plt.subplot(313)
	plt.hist(im[:,:,2].flatten(),256,range=(0,255),fc='r')
	plt.xlim(0,255)
	plt.show()


