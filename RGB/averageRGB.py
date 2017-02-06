#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread('../IMG/sample.png')

average_color_per_row = np.average(img,axis=0)

average_color = np.average(average_color_per_row,axis=0)

average_color = np.uint8(average_color)
print(average_color)
