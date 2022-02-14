import cv2.cv2 as cv2


def nothing(x):
    pass


img1 = cv2.imread("aircraft.jpg")
img1 = cv2.resize(img1, (640, 480))

img2 = cv2.imread("balls.jpg")
img2 = cv2.resize(img2, (640, 480))

output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.namedWindow("Transition Program")

cv2.createTrackbar("Alpha Beta", "Transition Program", 0, 1000, nothing)

while True:
    cv2.imshow("Transition Program", output)
    alpha = cv2.getTrackbarPos("Alpha Beta", "Transition Program") / 1000
    beta = 1 - alpha
    # formul alpha+beta=1
    # print(alpha, beta)

    output = cv2.addWeighted(img1, alpha, img2, beta, 0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
