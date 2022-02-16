import cv2.cv2 as cv2

img = cv2.imread("car.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

car_cascade = cv2.CascadeClassifier("C:\\python_repos\\openCV\\haar_cascade\\car.xml")

cars = car_cascade.detectMultiScale(gray, 1.1, 1)

for x, y, w, h in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
