import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()

    low = np.array([0,0,120])
    high = np.array([120,120,255])
    cv2.imshow('red',frame)
    cv2.waitKey(100)

cap.release()
cv2.destroyAllWindows()
