import cv2

img = cv2.imread("./../../data/elma.jpg",0)
image = cv2.imread("./../../data/elma.jpg",1)



def grayFilter(image):
    height, width, depth = image.shape
    for x in range(width):
        for y in range(height):
            ort = (int(image[y,x,0]) + int(image[y,x,1]) + int(image[y,x,2]))/3
            image[y,x,0:3] = ort


grayFilter(image)

cv2.imshow("Taken Gray Image",img)
cv2.imshow("Avarage Gray Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()