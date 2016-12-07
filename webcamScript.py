""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy
import time

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read() #gets the frame
    orangeLower=numpy.array([5, 50, 150], dtype="uint8") #uint8 necessary for this kind of thing 
    orangeUpper=numpy.array([100, 200, 255], dtype= "uint8") #represents upper and lower bounds of the color "red"

    mask=cv2.inRange(frame, orangeLower,orangeUpper) #creates mask of all the red pixels
    output=cv2.bitwise_and(frame,frame,mask=mask) #maps mask onto image

    output = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
    output = cv2.erode(output, None, iterations=2)
    output = cv2.dilate(output, None, iterations=2)


###Detection part
    cv2.imshow('Colors', output) #display filtered out thing
    for row in output:
        for pixel in row:
            if pixel is not [0,0,0]:
               #print "detected!"
               pass

    # Display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
