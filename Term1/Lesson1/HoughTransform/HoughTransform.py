#import the dependencies
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#Read the image
image = mpimg.imread("laneimage1.jpg")
grey = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

#Define the kernel for the gaussian blur
kernel = 5

#Apply the gausssian blur
gaussian_blur = cv2.GaussianBlur(grey,(kernel,kernel),0)

#Define the threshold for the Canny edge
low_thrsld = 100
high_thrsld = 200

#Detect canny edges
canny_edge = cv2.Canny(gaussian_blur,low_thrsld,high_thrsld)

# Create a masked edges image using fillPoly()
mask = np.zeros_like(canny_edge)
ignore_mask_color = 255
imshape = image.shape
vertices = np.array([[(0,imshape[0]),(0.45*imshape[1], 0.6*imshape[0]), (0.55*imshape[1], 0.6*imshape[0]), (imshape[1],imshape[0])]], dtype=np.int32)
cv2.fillPoly(mask, vertices, ignore_mask_color)
masked_edges = cv2.bitwise_and(canny_edge, mask)

#Parameters for Hough transform
rho = 1
theta = np.pi/180
threshold = 10
min_line_length = 100
max_line_gap = 10

#Blank image
line_image = np.copy(image)*0

#Perform hough transform to find line in the canny edge image
lines = cv2.HoughLinesP(masked_edges,rho, theta, threshold, np.array([]),
                        min_line_length, max_line_gap)

#Iterate and draw lines
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

# Create a "color" binary image to combine with line image
color_edges = np.dstack((canny_edge, canny_edge, canny_edge))

# Draw the lines on the edge image
combo = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)

#Show the image
plt.imshow(combo)
plt.show()
