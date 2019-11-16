import cv2

cap = cv2.VideoCapture("./../../data/shuttle.mp4")

while cap.isOpened():
    ret,frame = cap.read()

    if ret == True:

        # frame[:, :, 0] = 0
        # frame[:, :, 1] = 0
        # frame[:, :, 2] = 0

        # blur = cv2.bilateralFilter(frame,7,50,50)
        # edgesNormal = cv2.Canny(frame,100,200)
        # edges = cv2.Canny(blur, 100, 200)

        # cv2.imshow("Canny Edges With Bilateral Video",edges)
        # cv2.imshow("Canny Edges",edgesNormal)


        cv2.imshow("Shuttle Video with Color Filters",frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
