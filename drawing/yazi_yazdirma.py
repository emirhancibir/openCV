import cv2.cv2 as cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

font1 = cv2.FONT_HERSHEY_PLAIN
font2 = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(canvas,"openCV",(30,150),font2,4,(0,0,0),thickness=3,lineType=cv2.LINE_AA)
"""
koordinat (x,y) ekseni
kordinat olarak orijini, yazının sol alt kosesi alır 
"""


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()