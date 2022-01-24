import cv2.cv2 as cv2
import numpy as np

cap = cv2.VideoCapture("dog.mp4")

while True:
    ret, frame = cap.read()
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    sensitivity = 15
    lower_white = np.array([0, 0, 255 - sensitivity])
    upper_white = np.array([255, sensitivity, 255])

    mask = cv2.inRange(hsv_img, lower_white, upper_white)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    if ret == False:
        break
    if cv2.waitKey(15) & 0xFF == ord("q"):
        break

cap.release
cv2.destroyAllWindows()
