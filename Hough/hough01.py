#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import pylab as plt

cups = cv2.imread('cups.jpg')
 
cups_preprocessed  = cv2.cvtColor(cv2.GaussianBlur(cups, (7,7), 0), cv2.COLOR_BGR2GRAY)
 
_, cups_thresh = cv2.threshold(cups_preprocessed, 200, 255, cv2.THRESH_BINARY)

cups_edges = cv2.Canny(cups_preprocessed,threshold1=90,threshold2=110)
#plt.imshow(cv2.cvtColor(cups_edges,cv2.COLOR_GRAY2RGB))

cups_lines = np.copy(cups)

num_pix_threshold = 110
lines = cv2.HoughLines(cups_edges,1,np.pi/180,num_pix_threshold)

for rho,theta in lines[0]:
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a * rho
	y0 = b * rho

	x1 = int(x0+1000*(-b))
	y1 = int(y0+1000*(a))

	x2 = int(x0-1000*(-b))
	y2 = int(y0-1000*(a))

	cv2.line(cups_lines,(x1,y1),(x2,y2),(0,0,255),1)

cv2.imshow('cups',cups_lines)
cv2.waitKey(0)
cv2.destroyAllWindows()
