# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:55:06 2020

@author: khushi shah
"""

import cv2
import sys

facecascade=cv2.CascadeClassifier('C:/Users/khushi shah/Desktop/haarcascade_frontalface_default.xml')
image=cv2.imread('C:/Users/khushi shah/Downloads/IMG-20200204-WA0157.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces=facecascade.detectMultiScale(gray,scaleFactor=2.05,minNeighbors=2,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)

print("Found {0} faces!".format(len(faces)))

for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    
cv2.imshow("Faces found",image)
cv2.waitKey(0)