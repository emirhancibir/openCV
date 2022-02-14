import cv2.cv2 as cv2

face_cascade = cv2.CascadeClassifier("C:\\python_repos\\openCV\\haar_cascade\\frontalface.xml")
eye_cascade = cv2.CascadeClassifier("C:\\python_repos\\openCV\\haar_cascade\\eye.xml")

cap = cv2.VideoCapture(0)

while 1:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        roi = frame[y:y + h, x:x + w]
        gray2 = gray[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(gray2, 1.3, 5)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
