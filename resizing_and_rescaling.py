import cv2 as cv

#changing the resolutiion of the video and only for live video
def changeRes(weidth, height):
    capture.set(3, weidth)
    capture.set(4, height)

def rescaleFrame(frame,scale = 0.75):
    # Images, videos, Live Videos
    width = int(frame.shape[1] * scale)

    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions , interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(r"C:\Users\Aryan Thapa\Desktop\a.mp4")
img = cv.imread(r"C:\Users\Aryan Thapa\Desktop\aryan.jpg")
resized_image = rescaleFrame(img)
cv.imshow('Imaged', resized_image)




while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
# Wait for a key press and close the window
cv.waitKey(0)
cv.destroyAllWindows()



