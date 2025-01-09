import cv2 as cv
import numpy as np
#Masking helps to remove all the unwanted parts of the image

img = cv.imread(r"C:\Users\Aryan Thapa\Desktop\aryan.jpg")
cv.imshow("Mine", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("Blank Image", blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Masked", mask)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow("Masked_Image", masked)
#we can also use rectangle instead of circle

cv.waitKey(0)