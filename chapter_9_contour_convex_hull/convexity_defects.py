import cv2.cv2 as cv2

img = cv2.imread("star.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, 0)

contours, _ = cv2.findContours(thresh, 2, 1)
cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)
"""
The output contains an array where each row contains 4 values 
[start point, endpoint, farthest point, approximate distance to the farthest point].
"""

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    # defects (yildizin ici yani kusur noktalari) 4 deger dondurur bu degerleri s,e,f,d degiskenlerine esitliyoruz
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, (0, 255, 0), 2, 8)
    cv2.circle(img, far, 5, (0, 0, 255), -1)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
src:
https://theailearner.com/2020/11/09/convexity-defects-opencv/#:~:text=OpenCV%20provides%20a%20function%20cv2,the%20convexity%20defects%20as%20output.
"""
