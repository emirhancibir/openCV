import cv2.cv2 as cv2

vid = cv2.VideoCapture("faces.mp4")
face_cascade = cv2.CascadeClassifier("C:\\python_repos\\openCV\\haar_cascade\\frontalface.xml")

while True:
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break
    if ret == 0:
        break

vid.release()
cv2.destroyAllWindows()
