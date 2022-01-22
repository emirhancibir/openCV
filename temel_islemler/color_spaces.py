import cv2.cv2 as cv2

img = cv2.imread("lena.jpg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("BGR IMG",img)
cv2.imshow("RGB IMG",img1)
cv2.imshow("HSV IMG",img2)


cv2.waitKey(0)
cv2.destroyAllWindows()