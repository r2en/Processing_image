#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread('coin.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_pp = cv2.GaussianBlur(img_gray,(5,5),0)

ret,thresh = cv2.threshold(img_pp,130,255,cv2.THRESH_BINARY)

thresh = cv2.bitwise_not(thresh)
plt.imshow(thresh)
plt.show()
