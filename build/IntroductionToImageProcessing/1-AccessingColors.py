import cv2
import numpy as np

img = cv2.imread('./../../data/elma.jpg',1) #Intr.->build->create.->data->elma.jpg

convert = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#       elma.jpg için genişlik:640 yükseklik:512 pixel
height, width, depth = img.shape # 640,512,3
#       Kontrol et -> print(width)
#       Depth = 0 yaparsam ne olur ?

for x in range(width):
    for y in range(height):
        img[y,x,0] = 0
        img[y,x,1] = 0
        img[y,x,2] = 0
        #img[y,x] = [0,0,0]


img[:,:,0] = 255
img[:,:,1] = 255

# : = 0:height, 0:width

cv2.imshow("Image",img)
cv2.imshow("HSV", convert)
cv2.waitKey(0)
cv2.destroyAllWindows()
