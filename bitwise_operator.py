import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1)
circle = cv.circle(blank.copy(),(200,200),200,255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#1. bitwise and operation
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("AND", bitwise_and)

#2.bitwise or
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("OR", bitwise_or)

#3. bitwise _xor --> non- intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("XOR", bitwise_xor)

#4. bitwise_not
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Not", bitwise_not)


cv.waitKey(0)