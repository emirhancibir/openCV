import cv2.cv2 as cv2

cap = cv2.VideoCapture("eye_motion.mp4")

while True:
    ret, frame = cap.read()

    if ret == False:
        break
    roi = frame[80:210, 230:450]
    rows, cols, _ = roi.shape

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # goz bebegi siyah oldugu icin inverse binary siyah -> beyaz
    _, thresh = cv2.threshold(gray, 3, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    """
    Goz bebegi en buyuk kontur alanıdır
    key neyi referans alarak sıralayacagını belirler alanı kucukten buyuge sıralar sonra reverse = True
    oldugu icin alanı en buyuk olandan kucuk olana dogru siralanir
    """

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)

        # (x, y), radius = cv2.minEnclosingCircle(cnt)
        # center = (int(x), int(y))
        # radius = int(radius)
        # cv2.circle(roi, center, radius, (0, 255, 0), 2)
        break
    frame[80:210, 230:450] = roi
    # frame nin bu bolgesindeki degerleri islem yaptıgımız roiye ekliyoruz

    cv2.imshow("ROI", roi)
    cv2.imshow("frame", frame)
    cv2.imshow("thresh", thresh)

    if cv2.waitKey(80) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
