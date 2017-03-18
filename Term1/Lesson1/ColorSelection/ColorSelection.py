#import the dependencies
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#Read the image file
image = mpimg.imread('lane_image1.jpg')

#Get the size of the image
ysize = image[0]
xsize = image[1]

#Copy the image to another variable.This ensures changes doesn't modify original
image_copy = np.copy(image)

#Define the threshold below which we will be making the changes
red_thrsld = 180
blue_thrsld = 200
green_thrsld = 200

#Put the thresholds in an array
rgb_thrsld = [red_thrsld,green_thrsld,blue_thrsld]

#Get all the pixels which are below the mentioned thresholds
pixels_tobechanged = (image[:,:,0] < rgb_thrsld[0]) \
                    | (image[:,:,1] < rgb_thrsld[1]) \
                    | (image[:,:,2] < rgb_thrsld[2])

#Change those pixels to black
image_copy[pixels_tobechanged] = [0,0,0]

#Display the image
plt.imshow(image_copy)
plt.show()

#Save the image
mpimg.imsave("lane_image1_modified.jpg",image_copy)
