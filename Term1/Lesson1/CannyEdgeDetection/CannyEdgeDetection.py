#Import dependencies
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Read the image
image = mpimg.imread("exit-ramp.jpg")

#Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#Define the kernel size to apply gaussian blur
kernel = 5

#Apply the gaussian blur to supress any noise and spurious gradient in image
blur_gray = cv2.GaussianBlur(gray,(kernel,kernel),0)

#Define the threshold for the canny edge detection
#Strong edges(gradient) above this will be used as an edge
high_thrsld = 200

#Reject pixels below this threshold
low_thrsld = 100

#Do a canny edge detection on the gray scale image
edge = cv2.Canny(gray,low_thrsld,high_thrsld)

#Show the image
plt.imshow(edge, cmap = 'Greys_r')
plt.show()
