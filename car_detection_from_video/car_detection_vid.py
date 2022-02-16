import cv2.cv2 as cv2

car_cascade = cv2.CascadeClassifier("C:\\python_repos\\openCV\\haar_cascade\\car.xml")

cap = cv2.VideoCapture("car.mp4")

while 1:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 360))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.3, 3)

    for x, y, w, h in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    cv2.imshow("frame", frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
    if ret == 0:
        break

cap.release()
cv2.destroyAllWindows()
