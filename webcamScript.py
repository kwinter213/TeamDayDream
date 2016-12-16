
import cv2
import numpy
import time

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read() #gets the frame
    #orangeLower=numpy.array([5, 50, 150], dtype="uint8") #uint8 necessary for this kind of thing 
    #orangeUpper=numpy.array([100, 200, 255], dtype= "uint8") #represents upper and lower bounds of the color "orange"

    blackLower=numpy.array([0,0,0]) #black
    blackUpper=numpy.array([50, 50, 50])

    cv2.imshow('live feed', frame)
    mask=cv2.inRange(frame, blackLower,blackUpper) #creates mask of all the red pixels
    output=cv2.bitwise_and(frame,frame,mask=mask) #maps mask onto image

    #getting rid of false negatives and other outliers/smoothing over larger objects
    output = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
    output = cv2.erode(output, None, iterations=2)
    output = cv2.dilate(output, None, iterations=2)

    cv2.imshow('dilated', output)
    #conversion to find contours
    blurred = cv2.GaussianBlur(output, (7, 7), 0)
    edged = cv2.Canny(blurred, 50, 150)
    #imgray = cv2.cvtColor(edged, cv2.COLOR_BGR2GRAY)
    #ret, thresh= cv2.threshold(imgray,127,255,0)

    # find contours in the edge map
    contours, hierarchy= cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #drawing said contours (for debugging, not final)
    #cv2.drawContours(output, contours, -1, (255,0,0),-1)



    #returning/drawing the biggest rectangle
    minx=800
    maxx=0
    miny=800
    maxy=0
    for cnt in contours:
        x, y, w, h= cv2.boundingRect(cnt)
        if minx>x:
            minx=x
        if maxx<x+w:
            maxx=x+w
        if miny>y:
            miny=y
        if maxy<y+h:
            maxy=y+h
    cv2.rectangle(output, (minx,miny),(maxx-minx,maxy-miny),(0,255,0),2)
    #rect = cv2.minAreaRect(contours)
    #box = cv2.boxPoints(rect)
    #box = np.int0(box)
    #cv2.drawContours(img,[box],0,(0,0,255),2)

###Detection part
    cv2.imshow('Final with drawn rectangles', output) #display filtered out thing
    for row in output:
        for pixel in row:
            if pixel is not [0,0,0]:
               #print "detected!"
               pass

    # Display the resulting framegit pu
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()