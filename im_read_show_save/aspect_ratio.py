import cv2.cv2 as cv2


def resizeWithAspectRatio(img, width=None, height=None, inter=cv2.INTER_AREA):
    dimension = None

    (h, w) = img.shape[:2]
    """
    orijinal resmin boyutuna erişip (h,w) tuple sinin içine koyuor  0,1 i alır
    """

    if width is None and height is None:
        return img
    if width is None:
        r = height / float(h)
        dimension = (int(w * r), height)
        """
        r burada fonkda girdigimiz yüksekligin orjinal boyuta bolunmesi ile oran bulunur ve bu oran 
        en ile carpilarak ayni oranda en hesaplanir.
        mantigi su sekilde oran eşit olmalı a / b = a'/b'
        """
    else:
        r = width / float(w)
        dimension = (width, int(r * h))
    return cv2.resize(img, dimension, interpolation=inter)

img = cv2.imread("lena.jpg")

img_resized = resizeWithAspectRatio(img,height=144)

cv2.imshow("img",img)
cv2.imshow("resized_img",img_resized)

cv2.waitKey(0)
cv2.destroyAllWindows()