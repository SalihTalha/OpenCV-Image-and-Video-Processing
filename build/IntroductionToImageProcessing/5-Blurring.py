import cv2
import numpy as np
from matplotlib import pyplot as plt
# Low Pass Filter, görüntüyü bulanıklaştırmada kullanılır. Bu, görüntüdeki gürültüyü azaltmaya yarar.
# High Pass Filter, görüntüde kenarları bulmada kullanılır.
img = cv2.imread("./../../data/elma.jpg",0)

kernel = np.ones((9,9),np.float32)/81
# print(kernel)

dst = cv2.filter2D(img,-1,kernel)
dest = cv2.blur(dst,(9,9))
blur = cv2.GaussianBlur(img,(9,9),1)
median = cv2.medianBlur(img,5)
bilateral = cv2.bilateralFilter()

# print(dest)
# print(dst)

plt.subplot(121), plt.imshow(dst), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dest), plt.title('Blur')
plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()