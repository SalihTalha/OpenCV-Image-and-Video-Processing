import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame= cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#hue saturation value

    lower_range = np.array([0,0,0]) #RED
    upper_range = np.array([180,255,150])

    ourMask = cv2.inRange(hsv, lower_range,upper_range)
    result = cv2.bitwise_and(frame,frame,mask = ourMask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(ourMask,kernel,iterations=5)
    dilation = cv2.dilate(ourMask, kernel, iterations=5)

    opening = cv2.morphologyEx(ourMask,cv2.MORPH_OPEN,kernel)
    closing = cv2.morphologyEx(ourMask,cv2.MORPH_CLOSE,kernel)

    #cv2.imshow('frame',frame)
    cv2.imshow('mask',ourMask)
    #cv2.imshow('result',result)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()