import cv2.cv2 as cv2

img = cv2.imread("../temel_islemler/heli.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,-1,(0,0,255),2)

cv2.imshow("contours",img)

cv2.waitKey(0)
cv2.destroyAllWindows()