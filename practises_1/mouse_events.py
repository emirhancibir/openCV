import cv2.cv2 as cv2

cap = cv2.VideoCapture(0)

circles = []


def mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y))

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse)

while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    for center in circles:
        cv2.circle(frame, center, 20, (0, 0, 255), -1)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(2)

    if key & 0xFF == ord("q"):
        break

    if key == ord("c"):
        # circles ici bosaltılır
        circles = []

cap.release()
cv2.destroyAllWindows()
