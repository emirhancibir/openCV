import cv2.cv2 as cv2

body_cascade = cv2.CascadeClassifier("C:\\python_repos\\openCV\\haar_cascade\\fullbody.xml")

cap = cv2.VideoCapture("body.mp4")

while 1:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bodies = body_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    cv2.imshow("frame", frame)

    if cv2.waitKey(2) & 0xFF == ord("q"):
        break
    if ret == 0:
        break

cap.release()
cv2.destroyAllWindows()
