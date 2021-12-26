import cv2.cv2 as cv2

img = cv2.imread("lena.jpg")
"""
ilk parametre dosya yolunu uzantısı ile birlikte, ikinci parametre resimi nasıl okuyacagini belirtmek icin 
kullanilir cv2.IMREAD_GRAYSCALE gibi
"""

cv2.namedWindow("Image")
"""
cv2.WINDOW_NORMAL enables you to resize the window
"""

img = cv2.resize(img, (1920,1080))
cv2.imshow("Image",img)
# cv2.imwrite("lena_gray_read.jpg",img)

cv2.waitKey(0)
"""
birimi ms dir 0 giresek biz kapatana kadar acik kalir.
"""

cv2.destroyAllWindows()