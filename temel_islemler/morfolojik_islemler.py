import cv2.cv2 as cv2
import numpy as np

img = cv2.imread("heli.jpg", 0)
kernel = np.ones((4, 4), dtype=np.uint8)
"""
kernel matrisinin boyutunu arttirinca daha cok erozyona ugruyor
"""

eroded_image = cv2.erode(img, kernel, iterations=1)
dilated_image = cv2.dilate(img, kernel, iterations=1)
# dilate etmede 1 leri yani beyazları kalınlaştırıyor erozyonda ise 0 ları (siyahları) kalınlaştırır.
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("image", img)
# cv2.imshow("eroded_image",eroded_image)
# cv2.imshow("dilated_image",dilated_image)
# cv2.imshow("opened_image", opening)
# bu islem genelde goruntudeki beyaz (1) gurultuleri kaldırmak icin kullanılır
# cv2.imshow("closed_image",closing)
# bu islem genelde goruntudeki siyah (0) gurultuleri kaldırmak icin kullanılır
cv2.imshow("gradient_image", gradient)
# erode ve dilate islemlerinin farkinin alinmasiyla olusur

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
https://docs.opencv.org/3.4/d9/d61/tutorial_py_morphological_ops.html
"""
