#import the dependencies
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#Read the image file
image = mpimg.imread('lane_image1.jpg')

#Get the size of the image
ysize = image.shape[0]
xsize = image.shape[1]

#Copy the image to another variable.This ensures changes doesn't modify original
image_copy_color = np.copy(image)
image_copy_region = np.copy(image)

#Define the threshold below which we will be making the changes
red_thrsld = 180
blue_thrsld = 200
green_thrsld = 200

#Put the thresholds in an array
rgb_thrsld = [red_thrsld,green_thrsld,blue_thrsld]

#Vertices of the triangular mask
left_bottom_coords = [0,1.95*ysize/3]
top_center_coords = [xsize/2,ysize/2]
right_bottom_coords = [xsize,1.95*ysize/3]

#Get the lines from these coordinates
fit_left = np.polyfit((left_bottom_coords[0], top_center_coords[0]), \
                      (left_bottom_coords[1], top_center_coords[1]), 1)
fit_right = np.polyfit((right_bottom_coords[0],top_center_coords[0]),\
                       (right_bottom_coords[1], top_center_coords[1]), 1)
fit_bottom = np.polyfit((left_bottom_coords[0], right_bottom_coords[0]),\
                         (left_bottom_coords[1], right_bottom_coords[1]), 1)

#Get all the pixels which are below the mentioned thresholds
pixels_tobechanged = (image[:,:,0] < rgb_thrsld[0]) \
                    | (image[:,:,1] < rgb_thrsld[1]) \
                    | (image[:,:,2] < rgb_thrsld[2])

#Region threshold
X1 = np.arange(0, xsize)
Y1 = np.arange(0, ysize)
XX, YY = np.meshgrid(X1, Y1)
# print(XX)
# print(YY)

#This defines the region of interest. All y's greater than or less than
#the respective line
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))

#MAsk color and region selection
image_copy_color[pixels_tobechanged | ~region_thresholds] = [0,0,0]

# Color pixels red where both color and region selections met
image_copy_region[~pixels_tobechanged & region_thresholds] = [255, 0, 0]

#Display the image
plt.imshow(image_copy_region)
plt.show()

#Save the image
mpimg.imsave("lane_image1_modified.jpg",image_copy_region)
