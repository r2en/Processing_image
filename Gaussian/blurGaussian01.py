#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread('../blue.png')

img_blur01 = cv2.GaussianBlur(img,(11,11),0)
img_blur02 = cv2.GaussianBlur(img,(41,41),0)
img_blur03 = cv2.GaussianBlur(img,(61,61),0)

plt.subplot(221),plt.imshow(img)
plt.subplot(222),plt.imshow(img_blur01)
plt.subplot(223),plt.imshow(img_blur02)
plt.subplot(224),plt.imshow(img_blur03)

plt.show()
