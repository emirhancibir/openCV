import cv2.cv2 as cv2
import numpy as np

img = cv2.imread("lena.jpg")

dimension = img.shape
print(dimension)

color = img[510, 510]
print("BGR : ", color)
blue = img[510, 510, 0]
print("Blue :", blue)
green = img[510, 510, 1]
print("Green :", green)
red = img[510, 510, 2]
print("Red :", red)

blue1 = img.item(210, 210, 0)
print("blue1 : ", blue1)
img.itemset((210, 210, 0), 149)
print("new blue1 : ", img[210, 210, 0])

"""
Output:
(512, 512, 3)
[ 80  71 181]
Blue : 80
Green : 71
Red : 181
blue1 :  78
new blue1 :  149
"""

# img[220:512,310:512] = [0,255,0]

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
