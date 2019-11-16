import cv2

img = cv2.imread("./../../data/elma.jpg", 1)
height, width, depth = img.shape


def redFilter(image):
    image[0:height, 0:width, 0] = 0
    image[0:height, 0:width, 1] = 0


def greenFilter(image):
    image[0:height, 0:width, 0] = 0
    image[0:height, 0:width, 2] = 0


def blueFilter(image):
    image[0:height, 0:width, 1] = 0
    image[0:height, 0:width, 2] = 0

# image[:,:,1] = 0

#cv2.imshow("Red Filtered Image", redFilter(img))

cv2.waitKey(0)
cv2.destroyAllWindows()
