import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame= cap.read()
    #frame = cv2.GaussianBlur(frame,(5,5),0)    #

    #laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    #sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    #sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    edgesx = cv2.Canny(frame,50,500)
    edgesy = cv2.Canny(frame,500,50)
    cv2.imshow('frame',frame)
    #cv2.imshow('laplacian',laplacian)
    #cv2.imshow('sobelx',sobelx)
    #cv2.imshow('sobely',sobely)     # !benim kameramda düzgün çalışmıyor
    cv2.imshow('edgesx',edgesx)
    cv2.imshow('edgesy',edgesy)     # farkı göremedim


    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()