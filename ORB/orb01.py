import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('castel.jpg',0)

orb = cv2.ORB_create()

kp = orb.detect(img,None)

kp,des = orb.compute(img,kp)

img2 = cv2.drawKeypoints(img,kp,None,color=(0,255,0),flags=0)
plt.imshow(img2),plt.show()