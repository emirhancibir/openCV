import cv2.cv2 as cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
"""
q ya basıp ciktiginda herhangibir hata lamamk icin cv2.CAP_DSHOW kullanılır
"""
fileName = "C:\python_repos\openCV\webcam.avi"
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
"""
codec degerleri her uzantı icin degisebilir bu yazilan avi icin gecerlidir mpeg icin falan farklıdır 
bkz :https://www.fourcc.org/
"""
frameRate = 30
resolution = (640,480)
videFileOutput = cv2.VideoWriter(fileName, codec, frameRate,resolution)

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)
    videFileOutput.write(frame)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
videFileOutput.release()
cv2.destroyAllWindows()
