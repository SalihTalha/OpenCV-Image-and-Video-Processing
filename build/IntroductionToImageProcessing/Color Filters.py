import cv2

img = cv2.imread("./../../data/elma.jpg",1)
height, width, depth = img.shape

def redFilter(img):
    img[0:height,0:width,0] = 0
    img[0:height,0:width,1] = 0

def greenFilter(img):
    img[0:height, 0:width, 0] = 0
    img[0:height, 0:width, 2] = 0

def blueFilter(img):
    img[0:height, 0:width, 1] = 0
    img[0:height, 0:width, 2] = 0

greenFilter(img)

cv2.imshow("Red Filtered Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()