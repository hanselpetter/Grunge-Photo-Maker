import cv2
import numpy as np

# load image
img1 = cv2.imread("image.png")
img2 = cv2.imread("IMG_1367.jpeg")

# convert to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# blur
blur1 = cv2.GaussianBlur(gray1, (0,0), sigmaX=13, sigmaY=13)
blur2 = cv2.GaussianBlur(gray2, (0,0), sigmaX=13, sigmaY=13)

# divide
divide1 = cv2.divide(gray1, blur1, scale=255)
divide2 = cv2.divide(gray2, blur2, scale=255)

# threshold
thresh1 = cv2.threshold(divide1, 200, 255, cv2.THRESH_BINARY)[1]
thresh2 = cv2.threshold(divide2, 200, 255, cv2.THRESH_BINARY)[1]

# morphology
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
morph1 = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
morph2 = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
morph1 = cv2.morphologyEx(morph1, cv2.MORPH_CLOSE, kernel)
morph2 = cv2.morphologyEx(morph2, cv2.MORPH_CLOSE, kernel)


# write result to disk
cv2.imwrite("img1_division_normalize.jpg", divide1)
cv2.imwrite("img2_division_normalize.jpg", divide2)
cv2.imwrite("img1_division_morph1.jpg", morph1)
cv2.imwrite("img1_division_morph2.jpg", morph2)


# display it
cv2.imshow("img1_norm", divide1)
cv2.imshow("img2_norm", divide2)
cv2.imshow("img1_thresh", thresh1)
cv2.imshow("img2_thresh", thresh2)
cv2.imshow("img1_morph", morph1)
cv2.imshow("img2_morph", morph2)
cv2.waitKey(0)
cv2.destroyAllWindows()