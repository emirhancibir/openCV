import cv2.cv2 as cv2

img = cv2.imread("starwars.jpg")
blur = cv2.medianBlur(img, 7)

cv2.imshow("img", img)
laplacian = cv2.Laplacian(blur, cv2.CV_64F).var()

print(laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
