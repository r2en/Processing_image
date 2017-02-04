#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('sample.png',cv2.IMREAD_UNCHANGED)

cv2.imshow('Unchanged',img)

key = cv2.waitKey(0)

if key == 27:
	cv2.destroyAllWindows()
elif key == ord('s'):
	cv2.imwrite('Unchanged.jpg',img)
	cv2.destroyAllWindows()
