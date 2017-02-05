#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2

img = cv2.imread('Oasis.jpg')

origsize = img.shape[:2][::-1]

img = cv2.resize(img,(origsize[0]/20,origsize[1]/20))

img = cv2.resize(img,origsize,interpolation = cv2.cv.CV_INTER_NN)

cv2.imwrite('mosaicOasis.jpg',img)
cv2.imshow('mosaic',img)
cv2.waitKey(0)
cv2.destroyAllWindows()