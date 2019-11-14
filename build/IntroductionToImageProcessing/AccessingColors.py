import cv2
import numpy as np

img = cv2.imread('./../../data/elma.jpg',1) #Intr.->build->create.->data->elma.jpg

#       elma.jpg için genişlik:640 yükseklik:512 pixel
height, width, depth = img.shape
#       Kontrol et -> print(width)
#       Depth = 0 yaparsam ne olur ?

for x in range(width):
    for y in range(height):
        img[y,x,0] = 0
        img[y,x,1] = 0
        img[y,x,2] = 0
        #img[y,x] = [0,0,0]


img[0:height,0:width,0] = 255
img[0:height,0:width,1] = 255


cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
