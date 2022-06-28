# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2

# capture frames from a video
video_path = r'/home/nroede/Python/Scripts/learncv/intro/images/video.avi'
cap = cv2.VideoCapture(video_path)

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video file")

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier(r'/home/nroede/Python/Scripts/learncv/intro/cars.xml')

# loop runs if capturing has been initialized.
while (cap.isOpened()):
    # reads frames from a video
    ret, frames = cap.read()
    if ret == True:
        # convert to gray scale of each frames
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        # Detects cars of different sizes in the input image
        cars = car_cascade.detectMultiScale(gray, 1.1, 1, minSize=(30,30))

        # To draw a rectangle in each cars
        for (x,y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

        # Display frames in a window
        cv2.imshow('video2', frames)

        # Wait for Esc key to stop
        if cv2.waitKey(33) == 27:
            break

    else:
        break

# When everything done, release the video capture object
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()