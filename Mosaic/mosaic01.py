#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
img = cv2.imread('lena.jpg')
size = img.shape[:2][::-1]
img = cv2.resize(img,(size[0]/10,size[1]/10))
img = cv2.resize(img,size,interpolation = cv2.cv.CV_INTER_NN)

cv2.imshow('mosaic',img)
cv2.waitKey(0)
cv2.destroyAllWindows()