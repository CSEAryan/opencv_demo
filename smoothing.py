#done when there are a lot of noise in the images

import cv2 as cv


img = cv.imread(r"C:\Users\Aryan Thapa\Desktop\aryan.jpg")

cv.imshow("Mine",img)
#different bluring techniques
#1, Average -> pixel intensity will be the average of all the pixels surrounding
average = cv.blur(img, (3,3))
cv.imshow('Average', average)


#2. Gaussian blur ->its look more natural
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('GaussianBlur', gaussian)

#3. Median blur ->instead of finding the average of the surrounding pixel it finds median
# its not meant for high kernal size
median = cv.medianBlur(img, 3)
cv.imshow("median", median)

#4. Bilateral Bluring -> retain the edges surrounding pixel select garna ko lagi sigmaspace haru ho
bilateral = cv.bilateralFilter(img, 5, 15,15)
cv.imshow("Bilateral", bilateral)
cv.waitKey(0)