import cv2.cv2 as cv2
import numpy as np

img = np.zeros((10, 10, 3), dtype=np.uint8)
img[0,1] = (255,255,255)
img[1,2] = (255,0,0)
img[2,3] = (0,255,0)
img[3,4] = (0,0,255)

img = cv2.resize(img, (1000, 1000),interpolation=cv2.INTER_AREA)

print(img)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
