import cv2.cv2 as cv2

# Geometrik seklin moments func. yardimiyla agirlik merkezini bulma

img = cv2.imread("contour.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
# thresh degeri array tutar

M = cv2.moments(thresh)
# dictionary tutar

X = int(M["m10"] / M["m00"])
Y = int(M["m01"] / M["m00"])

cv2.circle(img, (X, Y), 4, (0, 0, 255), thickness=-1)

cv2.imshow("centroid", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
src
https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
"""