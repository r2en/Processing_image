import cv2
import numpy as np

img = cv2.imread('castel.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


detector = cv2.ORB_create()
kp = detector.detect(gray)

img=cv2.drawKeypoints(gray,kp,None)

cv2.imshow('sift_keypoints.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows