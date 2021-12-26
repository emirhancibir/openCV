import cv2.cv2 as cv2
import numpy as np

canvas = np.zeros((512,512,3),dtype=np.uint8) +255
"""
elemanlari 0 olan matrisler uretir (0,0,0) lık matris +255 dersek (255,255,255) => karsiligi siyahtir 
"""

print(canvas)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()