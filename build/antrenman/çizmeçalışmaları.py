# Python cv2 ile fotoğraf üzerinde çizimler yapma

import numpy as np
import cv2

img = cv2.imread("./../../data/blobs.png", 1)
width, height,channels = img.shape
print(height,width)


cv2.line(img, (0, 0), (width, height), (50, 250, 50), 10)
cv2.rectangle(img,(0,0),(width,width),(120,0,250),2)
cv2.circle(img, (width,width),200,(25,30,50),2)

pts = np.array([[0,0],[100,100],[200,500],[150,50]],np.int32)
cv2.polylines(img,[pts],1,(0,0,255),3)


cv2.imshow("Tarama", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
