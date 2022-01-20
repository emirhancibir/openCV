import cv2.cv2 as cv2

img = cv2.imread("lena.jpg")
cv2.imshow("img",img)
print(img.shape)

roi = img[220:390,230:380]
cv2.imshow("roi",roi)

cv2.waitKey(0)
cv2.destroyAllWindows()