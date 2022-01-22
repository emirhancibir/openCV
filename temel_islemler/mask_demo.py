import cv2.cv2 as cv2
import numpy as np

cap = cv2.VideoCapture(0)


def nothing(x):
    pass


cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 500, 500)

cv2.createTrackbar("Lower - H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Lower - S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Lower - V", "Trackbar", 0, 255, nothing)
"""
Hue degeri range i 0,180 arasıdır
"""
cv2.createTrackbar("Upper - H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Upper - S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper - V", "Trackbar", 0, 255, nothing)

cv2.setTrackbarPos("Upper - H", "Trackbar", 180)
cv2.setTrackbarPos("Upper - S", "Trackbar", 255)
cv2.setTrackbarPos("Upper - V", "Trackbar", 255)
"""
trackbarın varsayılan olarak nerede durması gerektigini belirlemek icin kullanıyoruz
"""

while (1):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("Lower - H", "Trackbar")
    lower_s = cv2.getTrackbarPos("Lower - S", "Trackbar")
    lower_v = cv2.getTrackbarPos("Lower - V", "Trackbar")

    upper_h = cv2.getTrackbarPos("Upper - H", "Trackbar")
    upper_s = cv2.getTrackbarPos("Upper - S", "Trackbar")
    upper_v = cv2.getTrackbarPos("Upper - V", "Trackbar")

    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(frame_hsv, lower_color, upper_color)
    """
    bu foksiyonumuz ise girilen değerler arasındaki renkleri seçmeye yarar. Mesela mavi rengin taban ve tavan 
    renklerini girersek fonksiyona, kolaylıkla mavi rengi görüntümüz arasından seçebiliriz.
    """

    cv2.imshow("Original", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
