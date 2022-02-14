import cv2.cv2 as cv2

vid = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("C:\\python_repos\\openCV\\haar_cascade\\frontalface.xml")

while True:
    _, frame = vid.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.6, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


vid.release()
cv2.destroyAllWindows()
