import cv2.cv2 as cv2

img = cv2.imread("eye.png")

face_cascade = cv2.CascadeClassifier("C:\\python_repos\\openCV\\haar_cascade\\frontalface.xml")
eye_cascade = cv2.CascadeClassifier("C:\\python_repos\\openCV\\haar_cascade\\eye.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

img2 = img[y:y + h, x:x + w]
gray2 = gray[y:y + h, x:x + w]

# eye detection
eyes = eye_cascade.detectMultiScale(gray2)

for (ex, ey, ew, eh) in eyes:
    cv2.rectangle(img2, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 1)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
