# Geometrik seklin alaninin ve cevresinin hesaplanmasi
import cv2.cv2 as cv2

img = cv2.imread("contour.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# contour area ile alan
cnt = contours[0]
area = cv2.contourArea(cnt)
print(area)

# moments ile alan
M = cv2.moments(cnt)
print(M["m00"])

# triangle img perimeter
perimeter = cv2.arcLength(cnt, True)
print(perimeter)

cv2.waitKey(0)
cv2.destroyAllWindows()
