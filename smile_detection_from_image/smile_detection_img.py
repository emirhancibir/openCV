import cv2.cv2 as cv2

img = cv2.imread("smile.jpg")

face_cascade = cv2.CascadeClassifier("C:\\python_repos\\openCV\\haar_cascade\\frontalface.xml")
smile_cascade = cv2.CascadeClassifier("C:\\python_repos\\openCV\\haar_cascade\\smile.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
    # determine roi for face
    img2 = img[y:y + h, x:x + w]
    gray2 = gray[y: y + h, x:x + w]

# smile detection
smiles = smile_cascade.detectMultiScale(gray2, 1.5, 7)

for ex, ey, ew, eh in smiles:
    cv2.rectangle(img2, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
