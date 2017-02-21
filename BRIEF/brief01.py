import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('castel.jpg',0)

star = cv2.xfeatures2d.StarDetector_create()

brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

kp = star.detect(img,None)

kp,des = brief.compute(img,kp)

print brief.descriptorSize()
print des.shape
