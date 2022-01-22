import cv2.cv2 as cv2

cap = cv2.VideoCapture("1.mp4")

while True:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret == False:
        break

    # cv2.imshow("BGR", frame)
    cv2.imshow("gray", frame_gray)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
