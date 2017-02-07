#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import cv2

img01 = cv2.imread('Lut.jpg', 1)
img02 = cv2.imread('LutImg.jpg', 1)

orgYCrCb = cv2.cvtColor(img01, cv2.COLOR_BGR2YCR_CB)
lutYCrCb = cv2.cvtColor(img02, cv2.COLOR_BGR2YCR_CB)

histOrgY = cv2.calcHist([orgYCrCb], [0], None, [256], [0, 256])
histLutY = cv2.calcHist([lutYCrCb], [0], None, [256], [0, 256])

plt.plot(histOrgY)
plt.plot(histLutY)
plt.xlim([0, 256])
plt.show()