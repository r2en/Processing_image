import numpy as np
import cv2
import pylab as plt

img = cv2.imread('../sample.png',cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('gradient.jpeg',flags=0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

titles = 'BINARY'
images = thresh1

plt.imshow(images,'gray')
plt.title(titles)
plt.show()
