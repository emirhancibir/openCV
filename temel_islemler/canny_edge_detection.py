import cv2.cv2 as cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    edges = cv2.Canny(frame, 80, 200)

    cv2.imshow("frame", frame)

    cv2.imshow("edges", edges)
    if ret == 0:
        break
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
