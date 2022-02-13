import cv2.cv2 as cv2
import numpy as np
import requests


# url = "http://192.168.1.34:8080//shot.jpg"

# Trackbar olusturma
def nothing(x):
    pass


# Trackbar penceresi
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 500, 500)

cv2.createTrackbar("Lower - H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Lower - S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Lower - V", "Trackbar", 0, 255, nothing)

cv2.createTrackbar("Upper - H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Upper - S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper - V", "Trackbar", 0, 255, nothing)

# trackbar pos ları default atama
cv2.setTrackbarPos("Upper - H", "Trackbar", 180)
cv2.setTrackbarPos("Upper - S", "Trackbar", 255)
cv2.setTrackbarPos("Upper - V", "Trackbar", 255)

cap = cv2.VideoCapture(0)

x_range = np.arange(320, 326, 1)
y_range = np.arange(235, 246, 1)
# print(y_range[:])

while True:
    # img_resp = requests.get(url)
    # img_arr = np.array(bytearray(img_resp.content),dtype=np.uint8)
    # img = cv2.imdecode(img_arr,cv2.IMREAD_COLOR)
    # img = cv2.resize(img,(640,480))

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbar degerlerini alma
    lower_h = cv2.getTrackbarPos("Lower - H", "Trackbar")
    lower_s = cv2.getTrackbarPos("Lower - S", "Trackbar")
    lower_v = cv2.getTrackbarPos("Lower - V", "Trackbar")

    upper_h = cv2.getTrackbarPos("Upper - H", "Trackbar")
    upper_s = cv2.getTrackbarPos("Upper - S", "Trackbar")
    upper_v = cv2.getTrackbarPos("Upper - V", "Trackbar")

    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(hsv_img, lower_color, upper_color)

    sensitivity = 15
    lower_blue = np.array([120 - sensitivity, 100, 100])
    upper_blue = np.array([120 + sensitivity, 255, 255])

    kernel = np.ones((3, 3), np.uint8)

    # mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

    # yumusatma
    # erozyon ile
    # mask = cv2.erode(mask, kernel)
    # opening ile
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    cv2.imshow("mask", mask)

    M = cv2.moments(mask)

    if M["m10"] == 0:
        M["m10"] = 1

    if M["m00"] == 0:
        M["m00"] = 1

    if M["m01"] == 0:
        M["m01"] = 1

    # koordinat ekseni
    cv2.line(frame, (320, 0), (320, 480), (255, 0, 0), 4)
    cv2.line(frame, (0, 240), (640, 240), (255, 0, 0), 4)
    # center green circle
    cv2.circle(frame, (320, 240), 40, (0, 255, 0), 3)

    X = int(M["m10"] / M["m00"])
    Y = int(M["m01"] / M["m00"])

    if M["m01"] and M["m00"] and M["m10"] != 1:
        # object track circle
        cv2.circle(frame, (X, Y), 40, (0, 0, 255), 5)
        cv2.line(frame, (X, Y), (320, 240), (0, 0, 255), 3)


        # origin = (320,240)
        # print(X, "\n", Y)

        if x_range.__contains__(X) & y_range.__contains__(Y):
            cv2.putText(frame, "Hedefe Kilitlenildi!", (330, 420), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                        lineType=cv2.LINE_AA)
            # print("ortada")

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if ret == False:
        break

    if cv2.waitKey(15) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
