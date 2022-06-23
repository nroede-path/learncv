# Importing the OpenCV library
import cv2
import os

# Image path
image_path = r'/home/nroede/Python/Scripts/learncv/intro/images/introimg.jpg'

# Reading the image
image = cv2.imread(image_path)

# Extracting the height and width of an image
h, w = image.shape[:2]
# Displaying the height and width
print("Height = {}, Width = {}".format(h, w))

# Extracting RGB values.
# Here we have randomly chosen a pixel
# by passing in 100, 100 for height and width.
(B, G, R) = image[100, 100]

# Displaying the pixel values
print("R = {}, G = {}, B = {}".format(R, G, B))

# We can also pass the channel to extract
# the value for a specific channel
B = image[100, 100, 0]
print("B = {}".format(B))

# We will calculate the region of interest
# by slicing the pixels of the image
roi = image[100 : 500, 200 : 700]

# resize() function takes 2 parameters,
# the image and the dimensions
resize = cv2.resize(image, (800, 800))

# Calculating the ratio
ratio = 800 / w

# Creating a tuple containing width and height
dim = (800, int(h * ratio))

# Resizing the image
resize_aspect = cv2.resize(image, dim)

# Calculating the center of the image
center = (w // 2, h // 2)

# Generating a rotation matrix
matrix = cv2.getRotationMatrix2D(center, -45, 1.0)

# Performing the affine transformation
rotated = cv2.warpAffine(image, matrix, (w, h))

# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny edge detection.
edges = cv2.Canny(image, 100, 200)

# Denoising of image saving it into dst image
denoise = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)

# We are copying the original image,
# as it is an in-place operation.
output = image.copy()

# Using the rectangle() function to create a rectangle.
rectangle = cv2.rectangle(output, (1500, 900),
						(600, 400), (255, 0, 0), 2)
 
# Adding the text using putText() function
text = cv2.putText(output, 'OpenCV Demo', (500, 550),
				cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)

cv2.imshow('w0', image)
cv2.imshow('w1', roi)
cv2.imshow('w2', resize)
cv2.imshow('w3', resize_aspect)
cv2.imshow('w4', rotated)
cv2.imshow('w5', gray_image)
cv2.imshow('w6', edges)
cv2.imshow('w7', denoise)
cv2.imshow('w8', output)

# Using cv2.imshow() method
# Displaying the image

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)
  
# closing all open windows
cv2.destroyAllWindows()

# Image directory
directory = r'/home/nroede/Python/Scripts/learncv/intro/images'

# Change the current directory 
# to specified directory 
os.chdir(directory)

# List files and directories    
print("Before saving image:")  
print(os.listdir(directory))

cv2.imwrite('roi.jpg', roi)
cv2.imwrite('resize.jpg', resize)
cv2.imwrite('resize_aspect.jpg', resize_aspect)
cv2.imwrite('rotated.jpg', rotated)
cv2.imwrite('gray_image.jpg', gray_image)
cv2.imwrite('edges.jpg', edges)
cv2.imwrite('denoise.jpg', denoise)
cv2.imwrite('output.jpg', output)

# List files and directories   
print("After saving image:")  
print(os.listdir(directory))
  
print('Successfully saved')