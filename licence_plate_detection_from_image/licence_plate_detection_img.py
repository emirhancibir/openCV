import cv2.cv2 as cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import imutils

# img = cv2.imread("licence_plate.jpg")
img = cv2.imread("licence_plate2.png")



gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# smoothing
filter = cv2.bilateralFilter(gray_img, 6, 250, 250)  # 6,250,250
"""
 cv2.bilateralFilter() is highly effective in noise removal while keeping edges sharp.
 """
# find edges
edged = cv2.Canny(filter, 50, 200)
# find contours
contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(contours)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
"""
    key => sort by field reverse=> Reverse sort
    [:10] 0dan 10 a kadar olan
"""
screen = None
# approximation polygon
for c in cnts:
    epsilon = 0.018 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    if len(approx) == 4:
        screen = approx
        # screen dörtgenin koordinatlarını tutar
        break

# masking
mask = np.zeros(gray_img.shape, dtype=np.uint8)

new_img = cv2.drawContours(mask, [screen], 0, (255, 255, 255), -1)
new_img = cv2.bitwise_and(img, img, mask=mask)
"""
and fonksiyonu mask ie orjinal image çarpma işlemi yaptı siyah yerler 0 oldugu icin 
sadece beyaz bolge 0dan farklı oldu 
"""

# cropping plate

(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
# orjin ekranın sol üst kosesi
cropped = gray_img[topx:bottomx + 1, topy:bottomy + 1]
# +1 son degerlerde dahil olsun icin

text = pytesseract.image_to_string(cropped, lang="eng")
cv2.imshow("full_img", img)
cv2.imshow("img", cropped)

print("licence plate detected : ", text)

cv2.waitKey(0)
cv2.destroyAllWindows()
