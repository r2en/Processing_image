import numpy as np
import cv2
import pylab as plt

img = cv2.imread('../sample.png',cv2.IMREAD_GRAYSCALE)

piet = cv2.imread('../sample.png')
piet_hsv = cv2.cvtColor(piet,cv2.COLOR_BGR2HSV)

blue_min = np.array([100,100,100],np.uint8)
blue_max = np.array([140,255,255],np.uint8)
threshold_blue_img = cv2.inRange(piet_hsv,blue_min,blue_max)

threshold_blue_img = cv2.cvtColor(threshold_blue_img,cv2.COLOR_GRAY2RGB)
plt.imshow(img)
plt.show()

plt.imshow(threshold_blue_img)
plt.show()