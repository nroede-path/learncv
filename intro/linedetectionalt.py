# Python program to illustrate HoughLine method for line detection by directly obtaining line end points 

# Following second program in https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/

import cv2
import numpy as np

# Read image
image_path = r'/home/nroede/Python/Scripts/learncv/intro/images/brickpattern.jpg'
image = cv2.imread(image_path)

# Convert image to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Use canny edge detection
edges = cv2.Canny(gray,50,150,apertureSize=3)

# Apply HoughLinesP method to
# to directly obtain line end points
lines = cv2.HoughLinesP(
			edges, # Input edge image
			1, # Distance resolution in pixels
			np.pi/180, # Angle resolution in radians
			threshold=100, # Min number of votes for valid line
			minLineLength=5, # Min allowed length of line
			maxLineGap=10 # Max allowed gap between line for joining them
			)

# Iterate over points
for points in lines:
	# Extracted points nested in the list
	x1,y1,x2,y2=points[0]
	# Draw the lines joing the points
	# On the original image
	cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)

	
# Save the result image
cv2.imshow('detectedLines.png',image)
# waits for user to press any key (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)
  
# closing all open windows
cv2.destroyAllWindows()