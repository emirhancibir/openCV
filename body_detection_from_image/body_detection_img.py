import cv2.cv2 as cv2

img = cv2.imread("body1.jpg")

body_cascade = cv2.CascadeClassifier("C:\\python_repos\\openCV\\haar_cascade\\fullbody.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bodies = body_cascade.detectMultiScale(gray)

for (x, y, w, h) in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()