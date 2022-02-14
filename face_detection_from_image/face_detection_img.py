import cv2.cv2 as cv2

img = cv2.imread("face.png")
face_cascade = cv2.CascadeClassifier("C:\\python_repos\\openCV\\haar_cascade\\frontalface.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 8)
# faces type ı tuple dır 4 degişken ikisi yuzun sol ust koordinatı diger ikisi genislik ve yuksekligi
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
