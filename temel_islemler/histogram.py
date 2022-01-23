import cv2.cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("heli.jpg")
# img = np.zeros((500, 500), dtype=np.uint8) + 200
#
# cv2.rectangle(img, (50, 50), (220, 220), (255, 255, 255), -1)
# cv2.putText(img, "openCV", (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 3, cv2.LINE_AA)
# plt.hist(img.ravel(), 256, [0, 256])
# ravel fonksiyonu matrisi tek satıra doker cunku hist fonksiyonundaki x parametresi tek satır matris ister
b, g, r = cv2.split(img)
# bu fonksiyon resmin renk degerlerini ayirir
plt.subplot(3, 1, 1)
plt.hist(b.ravel(), 256, [0, 256], color='blue')

plt.subplot(3, 1, 2)
plt.hist(g.ravel(), 256, [0, 256], color='green')

plt.subplot(3, 1, 3)
plt.hist(r.ravel(), 256, [0, 256], color='red')

plt.show()

cv2.imshow("img", img)

"""
y ekseni 500*500 den 250000 pixel sayısını verir x ekseni de renk degerlerini siyah oldugu icin tum pixeller 0 dir
"""
cv2.waitKey(0)
cv2.destroyAllWindows()
