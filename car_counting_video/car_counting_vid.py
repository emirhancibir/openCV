import cv2.cv2 as cv2
import numpy as np

cap = cv2.VideoCapture("traffic.avi")
backsub = cv2.createBackgroundSubtractorMOG2()
c = 0

while 1:
    ret, frame = cap.read()
    if ret:
        fgmask = backsub.apply(frame)
        cv2.line(frame, (50, 0), (50, 300), (255, 0, 0), 2)
        cv2.line(frame, (70, 0), (70, 300), (255, 0, 0), 2)

        contours, hieararchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        try:
            hieararchy = hieararchy[0]
        except:
            hieararchy = []

        for contour, hier in zip(contours, hieararchy):
            (x, y, w, h) = cv2.boundingRect(contour)
            if w > 40 and h > 40:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                if x > 50 and x < 70:
                    c += 1

        cv2.putText(frame, "car : " + str(c), (200, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

        cv2.imshow("frame", frame)
        cv2.imshow("mask", fgmask)

        if cv2.waitKey(20) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
