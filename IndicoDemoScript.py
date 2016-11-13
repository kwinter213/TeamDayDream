import numpy as np
import cv2
import time

import indicoio
indicoio.config.api_key = 'd17e09c08d43f673f05743ec7304c9be'

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    time.sleep(.2) #a pause so that this doesn't process EVERY frame (twould be overly expensive/time-consuming)
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    highestProb=0
    highestItem='thing'
    print indicoio.image_recognition(frame)
    probDict= indicoio.image_recognition(frame) #returns a dictionary of 1000 "likely" items and the probability that it is the object...
    for item in probDict:
    	if(probDict[item]>highestProb): #finding the most likely object on the screen
    		highestProb=probDict[item]
    		highestItem=item
    print highestProb
    print highestItem

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()