#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as numpy
import sys
import os.path

def GetArguments(args):
	imagePath = args[1]
	cascade = ''

	if args[2] == '-face':
		cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')
	elif args[2] == '-eye':
		cascade = cv2.CascadeClassifier('./haarcascade_mcs_eyepair_big.xml')

	else:
		cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')

	rectThick = int(args[3])

	return imagePath,cascade,rectThick

def DetectAndMosaic(image,sascade,rectThick):

	if os.path.isfile(image) != True:
		exit()
	org = cv2.imread(image,cv2.IMREAD_COLOR)
	gray = cv2.cvtColor(org,cv2.COLOR_BGR2GRAY)
	faces = cascade.detectMultiScale(gray,1.1,5)

	size = org.shape[:2][::-1]

	resize = cv2.resize(org,(size[0]/10,size[1]/10))
	mosaic = cv2.resize(resize,size,interpolution = cv2.INTER_NEAREST)

	if len(faces) > 0:
		for x,y,w,h in faces:
			mosaicFace = mosaic[y:y+h,x:x+w]
			org[y:y+h,x:x+w] = mosaicFace
			cv2.rectangle(org,(x,y),(x+w,y+h),(0,0,255),thickness=rectThick)

	cv2.imshow('mosaic',org)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':

	args = sys.argv
	imageName,cascade,rectThick = GetArguments(args)
	DetectAndMosaic(imageName,cascade,rectThick)

