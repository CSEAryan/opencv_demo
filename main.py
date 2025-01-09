import cv2

# Load the image (using one of the methods mentioned above)
#image = cv2.imread(r'C:\Users\Aryan Thapa\Desktop\aryan.jpg')  # Raw string for the path

# Check if the image was successfully loaded
#if image is None:
    #print("Error: Image not found! Check the file path.")
   # exit()

# Display the image
#cv2.imshow("Image", image)

#Reading the video

capture = cv2.VideoCapture("C:\Users\Aryan Thapa\Desktop\plant_video.webm")
while True:
    isTrue, frame = capture.read()
    cv2.imshow('Video', frame)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
