import cv2
import numpy as np

img = cv2.imread("./../../data/koltuk.jpg",0)
height,width = img.shape

kernelX = np.zeros((3,3))
kernelX[0,0] = -1
kernelX[1,0] = -2
kernelX[2,0] = -1
kernelX[0,2] = 1
kernelX[1,2] = 2
kernelX[2,2] = 1
print(kernelX)

kernelY = np.zeros((3,3))
kernelY[0,0] = -1
kernelY[0,1] = -2
kernelY[0,2] = -1
kernelY[2,0] = 1
kernelY[2,1] = 2
kernelY[2,2] = 1
print(kernelY)

Blurred = cv2.GaussianBlur(img,(3,3),0)

edge = cv2.filter2D(img,0,kernelY)
edgeBlurred = cv2.filter2D(Blurred,0,kernelY)


cv2.imshow("Edge Detection After Blur",edgeBlurred)
cv2.imshow("Original",img)
cv2.imshow("EdgeDetection",edge)

cv2.waitKey(0)