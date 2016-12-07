##Kimberly Winter
#detects a specific color
#to be integrated into object recognition

import cv2
import numpy

#255, 144, 33
#color needs calibration, but yeah...
orangeLower=numpy.array([5, 50, 150], dtype="uint8") #uint8 necessary for this kind of thing 
orangeUpper=numpy.array([100, 200, 255], dtype= "uint8") #represents upper and lower bounds of the color "red"

image=cv2.imread("trafficCone.jpg") #image example
mask=cv2.inRange(image, orangeLower,orangeUpper) #creates mask of all the red pixels
output=cv2.bitwise_and(image,image,mask=mask) #maps mask onto image


cv2.imshow('Colors', output) #filtered out thing
cv2.waitKey(0)