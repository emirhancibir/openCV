import cv2.cv2 as cv2
import numpy as np

img = cv2.imread("aircraft.jpg")
img = cv2.resize(img, (320, 480))

img_2 = cv2.imread("aircraft_2.jpg")
img_2 = cv2.resize(img_2, (320, 480))

img_3 = cv2.medianBlur(img,5)
# birinci img pixellerinden ikincisini çıkarır ve diff img sine esitler
diff = cv2.subtract(img, img_3)

cv2.imshow("diff", diff)
b, g, r = cv2.split(diff)

if cv2.countNonZero(b) == 0 & cv2.countNonZero(g) == 0 & cv2.countNonZero(r) == 0:
    print("completely equal image")
else:
    print("not same image")

cv2.waitKey(0)
cv2.destroyAllWindows()
