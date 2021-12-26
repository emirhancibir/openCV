import cv2.cv2 as cv2

cap = cv2.VideoCapture("test_video.mp4")

# WebCam
# cap = cv2.VideoCapture()

""""
Neden boyle bir donguye ihtiyac var?
cunku opencv videoları frame frame okur ve biz bunu kapatana kadar yapmak istiyoruz bu yuzden sonsuz 
donguye ihtiyacimiz var
"""
while True:
    ret, frame = cap.read()

    if ret == 0:
        break
    """
    bu kosulda frame okunamadıginda ret degeri false olur ret false oldugunda donguyu kir
    """
    """
    .read fonksiyonu 2 deger doner birincisi frameleri  dogru mu okkudu true or false 
    ikincisi frameler bu yuzden iki degiskene ihtiyac var
    """
    frame = cv2.flip(frame, 1)
    """
    1 degeri y eksenine gore yansıtır
    0 means flipping around the x-axis and positive value (for example, 1) means flipping around y-axis.
    """
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    """
    if bloguda q tusuna bastiginda cikis yapmanı saglar
    waitkey i vermezsek hata verir cunku kac ms de okuayacagni bilmez
    """

cap.release()
cv2.destroyAllWindows()
