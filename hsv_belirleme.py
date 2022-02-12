import cv2.cv2 as cv2
import numpy as np

cap = cv2.VideoCapture("C:\\python_repos\\openCV\\hough_transforms\\line.mp4")

#trackbar icin bos fonks olusturma
def nothing(x):
    pass

# trackbar penceresi olusturma
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",500,500)

# trackbar olusturma
cv2.createTrackbar("Lower - H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Lower - S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Lower - V", "Trackbar", 0, 255, nothing)

cv2.createTrackbar("Upper - H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Upper - S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper - V", "Trackbar", 0, 255, nothing)

# trackbar ustdegerlerini set etme
cv2.setTrackbarPos("Upper - H", "Trackbar", 180)
cv2.setTrackbarPos("Upper - S", "Trackbar", 255)
cv2.setTrackbarPos("Upper - V", "Trackbar", 255)



while True:

    lower_h = cv2.getTrackbarPos("Lower - H", "Trackbar")
    lower_s = cv2.getTrackbarPos("Lower - S", "Trackbar")
    lower_v = cv2.getTrackbarPos("Lower - V", "Trackbar")

    upper_h = cv2.getTrackbarPos("Upper - H", "Trackbar")
    upper_s = cv2.getTrackbarPos("Upper - S", "Trackbar")
    upper_v = cv2.getTrackbarPos("Upper - V", "Trackbar")

    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    ret,frame = cap.read()
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_frame,lower_color,upper_color)

    cv2.imshow("frame",frame)
    cv2.imshow("mask", mask)




    if cv2.waitKey(15)  & 0xFF == ord("q"):
        break
    if ret == False:
        break


cap.release()
cv2.destroyAllWindows()

