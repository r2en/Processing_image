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

coins_and_contours = np.copy(coins)
 
min_coin_area = 60
large_contours = [cnt for cnt in coins_contours if cv2.contourArea(cnt) > min_coin_area]

cv2.drawContours(coins_and_contours, large_contours, -1, (255,0,0))

print('number of coins: %d' % len(large_contours))

cv2.imshow('image', coins_and_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()

