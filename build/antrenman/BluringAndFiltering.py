import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame= cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#hue saturation value

    lower_range = np.array([23,24,92])
    upper_range = np.array([255,255,255])

    ourMask = cv2.inRange(hsv, lower_range,upper_range)
    result = cv2.bitwise_and(frame,frame,mask = ourMask)
    kernel = np.ones((15,15),np.float32)/255
    smoothed = cv2.filter2D(result,-1,kernel)

    blur = cv2.GaussianBlur(result,(15,15),0)

    #deneme = cv2.bitwise_and(frame,frame,mask = cv2.inRange(cv2.GaussianBlur(hsv,(15,15),0),lower_range,upper_range))

    median = cv2.medianBlur(result,15)
    bilateral = cv2.bilateralFilter(result,15,75,75)
    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',ourMask)
    cv2.imshow('result',result)
    cv2.imshow('smoothed',smoothed)
    cv2.imshow('blur',blur)
    cv2.imshow('median',median)
    cv2.imshow('bilateral',bilateral)
    #cv2.imshow('blur', deneme)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()