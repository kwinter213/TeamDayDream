
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

    #getting rid of false negatives and other outliers/smoothing over larger objects
    output = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
    output = cv2.erode(output, None, iterations=2)
    output = cv2.dilate(output, None, iterations=2)

    #conversion to find contours
    blurred = cv2.GaussianBlur(output, (7, 7), 0)
    edged = cv2.Canny(blurred, 50, 150)
    #imgray = cv2.cvtColor(edged, cv2.COLOR_BGR2GRAY)
    #ret, thresh= cv2.threshold(imgray,127,255,0)

    # find contours in the edge map
    contours, hierarchy= cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    print len(contours[0])

    cnt = contours[0]


    #ctr = numpy.array(contours).reshape((-1,1,2)).astype(numpy.int32)
    #print len(ctr)
    #print type(ctr)
    #imgray=array2cv(cv2.cvtColor(cv2array(output), cv.CV_RGB2GRAY))
    #storage=cv.CreateMemStorage(0)
    cv2.drawContours(output, contours, -1, (255,0,0),-1)


###Detection part
    cv2.imshow('Colors', output) #display filtered out thing
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
