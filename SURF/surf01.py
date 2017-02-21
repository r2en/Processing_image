import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('castel.jpg',0)

surf = cv2.xfeatures2d.SURF_create(20000)
kp,des = surf.detectAndCompute(img,None)

img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()


