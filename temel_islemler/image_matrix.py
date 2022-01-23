import cv2.cv2 as cv2
import numpy as np

img = cv2.imread("lena.jpg", 0)
row, col = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
# 100 px row 50 pixel colon kaydirdi
dst = cv2.warpAffine(img, M, (row, col))
# print("Row : ",row,"\nColon : ",col)
cv2.imshow("img",img)
cv2.imshow("shifted img", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
src : https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html
"""
