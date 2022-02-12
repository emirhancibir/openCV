import cv2.cv2 as cv2
import numpy as np

img1 = cv2.imread("coins.jpg")
img2 = cv2.imread("balls.jpg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

gray1_blur = cv2.medianBlur(gray1, 5)
gray2_blur = cv2.medianBlur(gray2, 5)

circles = cv2.HoughCircles(gray1_blur, cv2.HOUGH_GRADIENT, 1, img1.shape[0] / 4 , param1=200, param2=10, minRadius=15,
                           maxRadius=80)

if circles is not None:
    circles = np.uint16(np.around(circles))
    """
    uc deger doner x,y,r
    x,y merkez koordinat r yarıcap 
    """

    for i in circles[0,:]:
        cv2.circle(img1,(i[0],i[1]),i[2],(0,0,255),2)

cv2.imshow("img",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()