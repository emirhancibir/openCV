import cv2.cv2 as cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

# Create trackbar window
cv2.namedWindow("Settings")
cv2.resizeWindow("Settings", 500, 500)

# create trackbar
cv2.createTrackbar("Lower H", "Settings", 0, 180, nothing)
cv2.createTrackbar("Lower S", "Settings", 0, 255, nothing)
cv2.createTrackbar("Lower V", "Settings", 0, 255, nothing)

cv2.createTrackbar("Upper H", "Settings", 0, 180, nothing)
cv2.createTrackbar("Upper S", "Settings", 0, 255, nothing)
cv2.createTrackbar("Upper V", "Settings", 0, 255, nothing)

cv2.setTrackbarPos("Upper H", "Settings", 180)
cv2.setTrackbarPos("Upper S", "Settings", 255)
cv2.setTrackbarPos("Upper V", "Settings", 255)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("Lower H", "Settings")
    lower_s = cv2.getTrackbarPos("Lower S", "Settings")
    lower_v = cv2.getTrackbarPos("Lower V", "Settings")

    upper_h = cv2.getTrackbarPos("Upper H", "Settings")
    upper_s = cv2.getTrackbarPos("Upper S", "Settings")
    upper_v = cv2.getTrackbarPos("Upper V", "Settings")

    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(hsv, lower_color, upper_color)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        epsilon = 0.01 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if area > 400:
        cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
        if len(approx) == 3:
            cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0), 5)
        elif len(approx) == 4:
            cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0), 5)
        elif len(approx) > 5:
            cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0), 5)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(15) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
