import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Aryan Thapa\Desktop\aryan.jpg")

cv.imshow('mine', img)

# Translation -> shifting an image

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated  = translate(img, -100, 100)
cv.imshow('translated',translated)

#rotation and we have to specify the point of rotation usually its the centre but we can also define it
def rotate(img,angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)
# we can specify the colockwise or anticlockwise by using positive or negative angle value
rotated= rotate(img,90)
cv.imshow('Rotated', rotated)


#flipping the image
#vertically
flip = cv.flip(img, 0)
cv.imshow('vertical', flip)

#horizental flip
flip2 = cv.flip(img, 1)
cv.imshow('hori', flip2)


#cropping
cropped = img[200:400, 300:400]
cv.imshow('cropped', cropped)


cv.waitKey(0)