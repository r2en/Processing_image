#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import pylab as plt

imgOrg = cv2.imread('Lut.jpg',1)
imgLut = cv2.imread('LutImg.jpg',1)

# convert BGR to YCrCb
orgYCrCb = cv2.cvtColor(imgOrg,cv2.COLOR_BGR2YCR_CB)
lutYCrCb = cv2.cvtColor(imgLut,cv2.COLOR_BGR2YCR_CB)

# histgram
histOrgY = cv2.calcHist([orgYCrCb],[0],None,[256],[0,256])
histLutY = cv2.calcHist([lutYCrCb],[0],None,[256],[0,256])

plt.plot(histOrgY)
plt.plot(histLutY)
plt.xlim([0,256])
plt.show()