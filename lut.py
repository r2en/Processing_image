#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import cv2

gamma = 1.8

lookUpTable  = np.zeros((256,1),dtype = 'uint8')

for i in range(256):
	lookUpTable[i][0] = 255 * pow(float(i)/255,1.0/gamma)

img_src = cv2.imread('Lut.jpg',1)

img_gamma = cv2.LUT(img_src,lookUpTable)

cv2.imwrite('lutImg.jpg',img_gamma)

cv2.imshow('lutImg',img_gamma)
cv2.waitKey(0)
cv2.destoryAllWindows()

