import cv2
import numpy as np

# Load image 
image = cv2.imread('./../data/blobs.png', 0)

#image = cv2.bitwise_not(image)

# Set our filtering parameters 
# Initialize parameter settiing using cv2.SimpleBlobDetector 
params = cv2.SimpleBlobDetector_Params()

# Set Area filtering parameters 
params.filterByArea = True
params.minArea = 80

# Set Circularity filtering parameters 
params.filterByCircularity = True
params.minCircularity = 0.5

# Set Convexity filtering parameters 
params.filterByConvexity = True
params.minConvexity = 0.3

# Set inertia filtering parameters 
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters 
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs 
keypoints = detector.detect(image)

# Draw blobs on our image as red circles 
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (0, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 100, 255), 1)

# Show blobs 
cv2.imshow("Filtering Circular Blobs Only", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows() 
