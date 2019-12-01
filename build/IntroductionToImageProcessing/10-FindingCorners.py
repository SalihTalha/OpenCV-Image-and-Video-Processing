import cv2
import numpy as np

imgC = cv2.imread("./../../data/no.jpg")
imgG = cv2.cvtColor(imgC, cv2.COLOR_BGR2GRAY)
imgG = np.float32(imgG)

corners = cv2.goodFeaturesToTrack(imgG, 500, 0.5, 10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(imgC, (x,y), 5, 255, -1)

cv2.imshow('Corners',imgC)
cv2.waitKey(0)
cv2.destroyAllWindows()