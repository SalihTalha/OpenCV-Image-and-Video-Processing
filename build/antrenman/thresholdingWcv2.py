import numpy as np
import cv2

img = cv2.imread("./../../data/elma.jpg")

retv,thold = cv2.threshold(img,120,255,cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

retv,thold2 = cv2.threshold(grayscaled,120,255,cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

retval,otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original',img)
cv2.imshow('threshold',thold)
cv2.imshow('thold2',thold2)
cv2.imshow('otsu',otsu)
cv2.imshow('gaus',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()

