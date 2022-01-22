import cv2.cv2 as cv2
import numpy as np

img_filter = cv2.imread("filter.png")
img_median = cv2.imread("median.png")
img_bilateral = cv2.imread("bilateral.png")

blur = cv2.blur(img_filter, (5, 5))
blur_gaussian = cv2.GaussianBlur(img_filter, (5, 5), cv2.BORDER_DEFAULT)
# blur2 = cv2.blur(img_filter,(6,6))
"""
kernel size tek sayi olmak zorunda
cift sayidada calisiyor neden?
duzeltme:
tek sayi oldugunda orijin etrafinda simetrik dagilir
bu da daha saglikli
"""
median_blur = cv2.medianBlur(img_median, 7)
"""
kernel burada tek sayi olamak zorunda 
"""
blur_bilateral = cv2.bilateralFilter(img_bilateral, 9, 75,75)
"""
d=9 , sigma color = 75 , sigma space = 75
d	Diameter of each pixel neighborhood that is used during filtering. If it is non-positive, it is computed from sigmaSpace.
sigmaColor	Filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood (see sigmaSpace) will be mixed together, resulting in larger areas of semi-equal color.
sigmaSpace	Filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough (see sigmaColor ). When d>0, it specifies the neighborhood size regardless of sigmaSpace. Otherwise, d is proportional to sigmaSpace.
"""

cv2.imshow("original", img_bilateral)
# cv2.imshow("blur",blur)
# cv2.imshow("gaussian_blur",blur2)
# cv2.imshow("median_blur", median_blur)
# cv2.imshow("blur_even",blur2)
cv2.imshow("bilateral_filter", blur_bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
