import cv2
import numpy as np

imgBGR = cv2.imread("./../../data/desenli.jpg",1)
img = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)

template = cv2.imread("./../../data/desenlilili.jpg",0) # as you can see i cant find a good image for this, you can searh for it


w, h = template.shape

res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
thold = 0.8

loc = np.where(thold <= res)

for pt in zip(*loc[::]):
    cv2.rectangle(imgBGR, pt, (pt[0]+w, pt[1]+h) ,(0,255,255), 2)

cv2.imshow('result',cv2.resize(imgBGR,(1080,720)))
cv2.waitKey(0)