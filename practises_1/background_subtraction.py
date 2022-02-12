import cv2.cv2 as cv2
import numpy as np

cap = cv2.VideoCapture("car.mp4")
_, first_frame = cap.read()
first_frame = cv2.resize(first_frame, (640, 480))
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
# yumusatma
fist_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    diff = cv2.absdiff(first_gray, gray)
    """
    OpenCV de arka plan temizleme işlemini absdiff metodu yapmaktadır. Absdiff metodu verilen iki matris arasında
    çıkarma işlemi yapar bu çıkarma işlemi sonucunda değişen kısımlar yani hareketli kısımlar gösterilir.Çıkarma 
    işlemi sonucu mutlak değer olarak döndürülür
    """

    cv2.imshow("frame", frame)
    cv2.imshow("first frame", first_frame)
    cv2.imshow("diff", diff)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
    elif ret == False:
        break

cap.release()
cv2.destroyAllWindows()
