# Standard imports
import cv2
import numpy as np;

# Nedense bu kod sonuç olarak görsel çıktı vermiyor, -1073741819 çıktısını verip hata vermeden sonlanıyor.

# Read image
im = cv2.imread("./../data/scan1.jpg", cv2.IMREAD_GRAYSCALE)

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector()

# Detect blobs.
keypoints = detector.detect(im)
cv2.imshow("key",keypoints)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
im_with_keypoints.save("./../data/result1.jpg") # Process finished with exit code -1073741819 (0xC0000005) , Image didnt saved
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()