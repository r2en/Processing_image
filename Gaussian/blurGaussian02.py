#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread('../blue.png')

blur01 = cv2.GaussianBlur(img,(11,11),0)
blur02 = cv2.GaussianBlur(img,(41,41),0)
blur03 = cv2.GaussianBlur(img,(61,61),0)

gray00 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
gray01 = cv2.cvtColor(blur01,cv2.COLOR_RGB2GRAY)
gray02 = cv2.cvtColor(blur02,cv2.COLOR_RGB2GRAY)
gray03 = cv2.cvtColor(blur03,cv2.COLOR_RGB2GRAY)

ret,thresh = cv2.threshold(gray00,127,255,cv2.THRESH_BINARY)
ret,thresh1 = cv2.threshold(gray01,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(gray02,127,255,cv2.THRESH_BINARY)
ret,thresh3 = cv2.threshold(gray03,127,255,cv2.THRESH_BINARY)

plt.subplot(221),plt.imshow(thresh)
plt.subplot(222),plt.imshow(thresh1)
plt.subplot(223),plt.imshow(thresh2)
plt.subplot(224),plt.imshow(thresh3)

plt.show()