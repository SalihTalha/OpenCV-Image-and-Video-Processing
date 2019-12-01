import cv2
import numpy as np

cap = cv2.VideoCapture("./../../data/traffic.mp4")
BGS = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    if ret == True:
        result = BGS.apply(frame)

        cv2.imshow('original', frame)
        cv2.imshow('result', result)

        if cv2.waitKey(1) & 0xFF == 'q':
            break

    else: break

cap.release()
cv2.destroyAllWindows()