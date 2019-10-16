import cv2
import math

img = cv2.imread("./../data/scan1.png", cv2.IMREAD_GRAYSCALE)
width, height, _ = img.shape()

tholdRenk = 20  # blob ne kadar karanlık olmadılır ? Ne kadar karanlık olan pikseller blob'a dahil edilecek?
tholdUzaklık = 25


class blobs:
    count = 0
    maxx = 0
    maxy = 0
    minx = 0
    miny = 0

    def __init__(self, Mx, My, mx, my):
        maxx = Mx
        maxy = My
        minx = mx
        miny = my

#TODO LİST
    # RGB UZAKLIK FONKSİYONU
    # İNT LOCATİON = X + Y * VİDEO.WİDHT
    #



    for w in width:
        for h in height:
            if img[w,h,0] + img[w,h,1] + img[w,h,2] < tholdRenk:
                for i in range(blobs.count):
                    if math.sqrt((w - list[i].maxx)**2 + (h - list[i].maxy)**2) > tholdUzaklık:
                        blobs a = new blobs()