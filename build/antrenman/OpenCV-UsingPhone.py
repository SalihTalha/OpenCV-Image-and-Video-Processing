import urllib.request
import cv2
import numpy as np
import time
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    URL = "http://172.28.10.207:8080/video"
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    cv2.imshow('IPWebcam', img)

    if cv2.waitKey(100):
        break

cv2.destroyAllWindows()