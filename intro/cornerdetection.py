# Detect up to N corners of an image (specified as 2nd parameter of goodFeaturestoTrack)

# Following https://www.geeksforgeeks.org/python-detect-corner-of-an-image-using-opencv/

# import the required library
import numpy as np
import cv2
from matplotlib import pyplot as plt


# Read image
image_path = r'/home/nroede/Python/Scripts/learncv/intro/images/chessboard.png'
img = cv2.imread(image_path)

# convert image to gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect corners with the goodFeaturesToTrack function.
corners = cv2.goodFeaturesToTrack(gray, 90, 0.01, 10)
corners = np.int0(corners)

# we iterate through each corner,
# making a circle at each point that we think is a corner.
for i in corners:
	x, y = i.ravel()
	cv2.circle(img, (x, y), 3, 255, -1)

plt.imshow(img), plt.show()
    
# De-allocate any associated memory usage (press q)
if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows()