import cv2.cv2 as cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255
"""
elemanlari 0 olan matrisler uretir (0,0,0) lık matris +255 dersek (255,255,255) => karsiligi siyahtir 
"""
# print(canvas)

cv2.line(canvas, (0, 0), (512, 512), (0, 0, 255), 5)
cv2.line(canvas, (0, 512), (512, 0), color=(0, 0, 255), thickness=5)

cv2.rectangle(canvas, (150, 150), (362, 362), color=(255, 0, 0), thickness=5)

cv2.circle(canvas, (256, 256), 100, (0, 255, 0), -1)

points = np.array([[150, 150], [250, 250], [300, 120]], np.int32)
cv2.polylines(canvas, [points], False, (0, 0, 255), thickness=4)

cv2.ellipse(canvas,(300,300),(80,20),0,90,360,(255,255,0),-1)
"""
axes en ve boy uzunluklarını verir
angle yatayl yaptıı acıyı verir
"""

cv2.imshow("Canvas", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
