import cv2.cv2 as cv2
import numpy as np

image = "starwars.jpg"
template = "starwars2.jpg"

img = cv2.imread(image)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread(template)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

res = cv2.matchTemplate(gray_img, gray_template, cv2.TM_CCOEFF_NORMED)
location = np.where(res >= 0.9)
# print(location)
"""
(array([52, 53, 53, 53, 54], dtype=int64), array([282, 281, 282, 283, 282], dtype=int64))
"""
h, w = gray_template.shape[::]
# -1 olmadan genişlik, yükseklik verir -1 ile yükseklik,genislik verir
for point in zip(*location[::-1]):
    # zip fonksiyonu iki listedeki eemanları birleştirmek için kullanıldı
    print(point)
    cv2.rectangle(img, point, (point[0] + w, point[1] + h), (255, 0, 0), 2)

# cv2.imshow("res", res)
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
