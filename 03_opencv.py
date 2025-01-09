#Drawing shapes and writing on images

import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('blank', blank)
#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Red', blank)


#draw a rectnagle
#cv.rectangle(blank, (0,0),(250,250),(0,250,0), thickness=2)
#Another way

#cv.rectangle(blank,(0,0),(250,500),(0,255,0), thickness=cv.FILLED)\

#alternative way
#img = cv.imread(r"C:\Users\Aryan Thapa\Desktop\aryan.jpg")
cv.rectangle(blank, (0,0),(blank.shape[1]//2 ,blank.shape[0]//2),(0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)


#3. Draw circle

cv.circle(blank,(blank.shape[1]//2 ,blank.shape[0]//2), 40,(0,0,255), thickness =-1)
cv.imshow('Circle', blank)
#img = cv.imread()
#cv.imshow('Cat', img)

#4. drawing a line
cv.line(blank,(0,0),(blank.shape[1]//2 ,blank.shape[0]//2),(255,255,255), thickness =3)
cv.imshow('line', blank)

#5.writing text on the image
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)


