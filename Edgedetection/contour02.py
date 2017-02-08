#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import pylab as plt

coins = cv2.imread('coins.jpg')
coins_gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
coins_preprocessed = cv2.GaussianBlur(coins_gray, (5, 5), 0)
 
_, coins_binary = cv2.threshold(coins_preprocessed, 130, 255, cv2.THRESH_BINARY)
 
coins_binary = cv2.bitwise_not(coins_binary)

coins_contours, _ = cv2.findContours(coins_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

bounding_img = np.copy(coins)
 
min_coin_area = 60
large_contours = [cnt for cnt in coins_contours if cv2.contourArea(cnt) > min_coin_area]

for contour in large_contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(bounding_img, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow('image', bounding_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
