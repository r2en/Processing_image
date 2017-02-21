import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('castel.jpg',0)

fast = cv2.FastFeatureDetector_create()

kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp,None,color=(255,0,0))

print "Threshold: ", fast.getThreshold()
print "nonmaxSuppression: ", fast.getNonmaxSuppression()
print "neighborhood: ", fast.getType()
print "Total Keypoints with nonmaxSuppression: ", len(kp)

cv2.imshow('fast_true',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)

print "Total Keypoints without nonmaxSuppression: ", len(kp)

img3 = cv2.drawKeypoints(img, kp,None,color=(255,0,0))

cv2.imshow('fast_false',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()