#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('luna.png',cv2.IMREAD_UNCHANGED)
cv2.imshow('sample.jpg',img)

key = cv2.waitKey(0)

if key == 27:
	cv2.destroyAllWindows()
elif key == ord('s'):
	cv2.imwrite('sample.jpg',img)
	cv2.destroyAllWindows()