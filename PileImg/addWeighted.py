#!/usr/bin/python
# -*- coding: utf-8 -*- 
import numpy as numpy
import cv2

imgA = cv2.imread("../IMG/BeatlesMono.jpg",1)
imgB = cv2.imread("../IMG/BeatlesColor.jpg",1)

print imgA.shape
print imgB.shape

img_03_07 = cv2.addWeighted(imgA,0.3,imgB,0.7,2.2)
img_05_05 = cv2.addWeighted(imgA,0.5,imgB,0.5,2.2)
img_07_03 = cv2.addWeighted(imgA,0.7,imgB,0.3,2.2)

cv2.imwrite("../IMG/Beatles0307.jpg",img_03_07)
cv2.imwrite("../IMG/Beatles0505.jpg",img_05_05)
cv2.imwrite("../IMG/Beatles0703.jpg",img_07_03)
