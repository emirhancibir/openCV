import cv2.cv2 as cv2
import numpy as np

img = cv2.imread("lena.jpg", 0)
row, col = img.shape

M = cv2.getRotationMatrix2D((col / 2, row / 2), 180, 1)
# saat yonu tersine dondurur

dst = cv2.warpAffine(img, M, (col, row))

cv2.imshow("img", img)
cv2.imshow("rotated_img", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
src : https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html
"""
