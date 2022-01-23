import cv2.cv2 as cv2

img = cv2.imread("heli.jpg", 0)

ret, th1 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,19,8)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,8)

cv2.imshow("img", img)
# cv2.imshow("img_th1", th1)
# cv2.imshow("img_th2", th2)
cv2.imshow("img_th3", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
