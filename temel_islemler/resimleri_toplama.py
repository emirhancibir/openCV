import cv2.cv2 as cv2
import numpy as np

circle = np.zeros((512, 512, 3), dtype=np.uint8) + 255
cv2.circle(circle, (256, 256), 60, (0, 0, 255), thickness=-1)

rectangle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(rectangle, (150, 150), (350, 350), (255, 0, 0), -1)

cv2.imshow("circle", circle)
cv2.imshow("rectangle", rectangle)

add = cv2.add(circle, rectangle)
# print(add[270, 270])
cv2.imshow("added", add)

cv2.waitKey(0)
cv2.destroyAllWindows()
