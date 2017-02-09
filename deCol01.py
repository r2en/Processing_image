#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import sys
import numpy as np

def decleaseColor(img):
    print type(img)
    rgb = cv2.split(img)

    for col in rgb:
        idx = np.where(col < 64)
        col[idx] = 32
        idx = np.where((64 <= col) & (col < 128))
        col[idx] = 96
        idx = np.where((128 <= col) & (col < 196))
        col[idx] = 160
        idx = np.where(196 <= col)
        col[idx] = 224 

    d_img = cv2.merge(rgb)
    return d_img

if __name__ == '__main__':

    img = cv2.imread('lena.jpg')
    d_img = decleaseColor(img)
    cv2.imshow('lena',d_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()