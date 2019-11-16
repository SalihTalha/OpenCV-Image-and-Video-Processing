import cv2
from ColorFilters import *
from GrayFilter import grayFilter

img = cv2.imread("./../../data/koltuk.jpg", 1)
red = cv2.imread("./../../data/koltuk.jpg", 1)
green = cv2.imread("./../../data/koltuk.jpg", 1)
blue = cv2.imread("./../../data/koltuk.jpg", 1)

height, width, depth = img.shape


red[0:height,0:width,0:3] = red[0:height,0:width,(2,2,2)]
green[0:height,0:width,0:3] = green[0:height,0:width,(1,1,1)]
blue[0:height,0:width,0:3] = blue[0:height,0:width,(0,0,0)]

#greenFilter(green)
#grayFilter(green)
#blueFilter(blue)
#grayFilter(blue)
#redFilter(red)
#grayFilter(red)
# YUKARIDAKİ YORUM SATIRLARINDAKİ ÖRNEK RESMİN PARLAKLIĞINI AZALTACAKTIR
cv2.imshow("red",red)
cv2.imshow("green",green)
cv2.imshow("blue",blue)
cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
