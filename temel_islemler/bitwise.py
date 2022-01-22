import cv2.cv2 as cv2

img1 = cv2.imread("bitwise_1.png")
img2 = cv2.imread("bitwise_2.png")

bit_and = cv2.bitwise_and(img1,img2)
bit_or = cv2.bitwise_or(img1,img2)
# siyah renk 0 beyaz renk 1'dir.

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("bit_or",bit_or)

cv2.waitKey(0)
cv2.destroyAllWindows()