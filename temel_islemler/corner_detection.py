import cv2.cv2 as cv2
import numpy as np

img = cv2.imread("contour.png")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = np.float32(gray_img)

corners = cv2.goodFeaturesToTrack(gray_img, 3, 0.01, 8)
# gray_img float32 tek kanal resim olmalı

corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    # ravel fonksiyonu tek dizi ye döker.
    cv2.circle(img, (x, y), 21, (0, 0, 255))

cv2.imshow("corners", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
