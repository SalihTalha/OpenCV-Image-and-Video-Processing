import cv2

cap = cv2.VideoCapture("./../../data/shuttle.mp4")

while (cap.isOpened()):
    ret,frame = cap.read()
    if ret==True:
        cv2.imshow("Original Video",frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:   # if ret == False -> No video capture -> break
        break

cap.release()
cv2.destroyAllWindows()
