import cv2.cv2 as cv2
import numpy as np

cap = cv2.VideoCapture(0)

x_range = np.arange(320, 326, 1)
y_range = np.arange(235, 246, 1)
# print(y_range[:])

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    sensitivity = 15
    lower_blue = np.array([120 - sensitivity, 100, 100])
    upper_blue = np.array([120 + sensitivity, 255, 255])

    kernel = np.ones((5, 5), np.uint8)

    mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
    #yumusatma
    mask = cv2.erode(mask,kernel)
    # res = cv2.bitwise_and(frame, frame, mask=mask)

    _, thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

    # cv2.imshow("thresh", thresh)

    M = cv2.moments(thresh)

    if M["m10"] == 0:
        M["m10"] = 1

    if M["m00"] == 0:
        M["m00"] = 1

    if M["m01"] == 0:
        M["m01"] = 1

    # koordinat ekseni
    cv2.line(frame, (320, 0), (320, 480), (255, 0, 0), 4)
    cv2.line(frame, (0, 240), (640, 240), (255, 0, 0), 4)
    # center black circle
    cv2.circle(frame, (320, 240), 40, (0, 255, 0), 3)

    X = int(M["m10"] / M["m00"])
    Y = int(M["m01"] / M["m00"])

    if M["m01"] and M["m00"] and M["m10"] != 1:
        cv2.circle(frame, (X, Y), 40, (0, 0, 255), 5)
        # origin = (320,240)
        # print(X, "\n", Y)

        if x_range.__contains__(X) & y_range.__contains__(Y):
            cv2.putText(frame, "Hedefe Kilitlenildi!", (330, 420), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                        lineType=cv2.LINE_AA)
            # print("ortada")

    cv2.imshow("frame", frame)
    # cv2.imshow("mask",mask)

    if ret == False:
        break

    if cv2.waitKey(15) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
