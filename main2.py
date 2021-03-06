# Software Design Final Project
# Team Daydream
# V1.0 - ERIC + KIM (only OpenCV)
# Changelog
# - Added basic overlay functionality

import cv2
import numpy
import time

MAXFRAMES=60    # max number of frames (length of animation)
NUM_FRAMES=36   # number of animation frames
OVERLAYFRAMERATE = 24
fc_overlay = 0  # frame count of overlay video
video_overlay=[]
overlay_x = 0
overlay_y = 0
overlay_w = 639 #64
overlay_h = 479 #64
overlay_starttime = 0
overlay_playing = False
stableTime=50 #iterations before average is taken-- used for stabilization

orangeLower=numpy.array([5, 50, 150])
orangeUpper=numpy.array([100, 200, 255]) #represents upper and lower bounds of the color "orange"
orangeCount=0 #used for cueing which set of images to use

greenLower=numpy.array([0,87, 39])
greenUpper=numpy.array([198,187, 139])
greenCount=1

blueLower=numpy.array([107,45,9])
blueUpper=numpy.array([207,145,109])
blueCount=2

redLower=numpy.array([0,0,67])
redUpper=numpy.array([72,84,167])
redCount=3

blackUpper=numpy.array([50, 50, 50])
blackLower=numpy.array([0,0,0]) #black
blackCount=4

colors=([orangeLower,orangeUpper,orangeCount],[greenLower,greenUpper,greenCount], [blueLower,blueUpper,blueCount],[redLower,redUpper,redCount], [blackLower,blackUpper, blackCount])

def loadOverlayVideo(col):
    """
    Load and generate overlay video, It's just for demo
    """
    global video_overlay
    video_overlay = []
    if(col[2]==0):#orange is priority
        mode = 1
        for i in range(1,NUM_FRAMES+1):
            # load 4-channel png image
            
            video_overlay.append(cv2.imread('maybe/' +str(i) + '.png', cv2.IMREAD_UNCHANGED))
        #return mode
    elif(col[2]==1): #then green
        mode = 1
        for i in range(1,NUM_FRAMES+1):
        # load 4-channel png image
            video_overlay.append(cv2.imread('maybe/'+str(i) + '.png', cv2.IMREAD_UNCHANGED))
        #return mode
    elif(col[2]==2): #then blue
        mode = 1
        for i in range(1,NUM_FRAMES+1):
        # load 4-channel png image
            video_overlay.append(cv2.imread('maybe/'+str(i) + '.png', cv2.IMREAD_UNCHANGED))
        #return mode
    elif(col[2]==3): #then red
        mode = 1
        for i in range(1,NUM_FRAMES+1):
        # load 4-channel png image
            video_overlay.append(cv2.imread('maybe/'+str(i) + '.png', cv2.IMREAD_UNCHANGED))
        #return mode
    elif(col[2]==4): #finally black
        mode = 2
        for i in range(1,NUM_FRAMES+1):
        # load 4-channel png image
            video_overlay.append(cv2.imread('maybe/'+str(i) + '.png', cv2.IMREAD_UNCHANGED))
        #return mode

def playoverlay(x, y):
    global overlay_playing, overlay_starttime, overlay_x, overlay_y
    overlay_playing = True
    overlay_starttime = time.clock()
    overlay_x = 400
    overlay_y = 300


def overlayFrame(frame):
    global overlay_playing
    centre_x=0
    centre_y=0 #centering the image
    # get frame number of overlay frame
    currTime = time.clock() - overlay_starttime
    if currTime > MAXFRAMES / OVERLAYFRAMERATE:
        overlay_playing = False
    frame_no = int(currTime * OVERLAYFRAMERATE) % NUM_FRAMES
    # composite overlay frame
    for c in range(0,3):
        
        alpha = video_overlay[frame_no][:,:,3] / 255.0
        color = video_overlay[frame_no][:,:,c] * (alpha)
        beta  = frame[centre_y : centre_y + overlay_h, centre_x : centre_x + overlay_w, c] * (1.0 - alpha)
        frame[centre_y : centre_y + overlay_h, centre_x : centre_x + overlay_w, c] = color + beta

def largeRectangle(frame,c): #finds the largest rectangle created in a frame by a black object, 1st input is image, 2nd input is color that is being searched for
    mask=cv2.inRange(frame, c[0], c[1]) #creates mask of all the pixels
    output=cv2.bitwise_and(frame,frame,mask=mask) #maps mask onto image

#getting rid of false negatives and other outliers/smoothing over larger objects
    output = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
    output = cv2.erode(output, None, iterations=2)
    output = cv2.dilate(output, None, iterations=2)

#cv2.imshow('dilated', output)
#conversion to find contours
    blurred = cv2.GaussianBlur(output, (7, 7), 0)
    edged = cv2.Canny(blurred, 50, 150)
#imgray = cv2.cvtColor(edged, cv2.COLOR_BGR2GRAY)
#ret, thresh= cv2.threshold(imgray,127,255,0)

# find contours in the edge map
    contours, hierarchy= cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #returning/drawing the biggest rectangle---- initial conditions unreasonable/will get reset
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
    return minx, maxx, miny, maxy, output

cap = cv2.VideoCapture(0)
cv2.namedWindow('cameraview')



#in order to take the average of the largest rectangle formed by the black mask/object
count=0
minxsum=0
maxxsum=0
minysum=0
maxysum=0



while(True):
    #initializing values
    minxAverage=0
    minyAverage=0
    maxxAverage=0
    maxyAverage=0
    # Capture frame-by-frame
    ret, frame = cap.read() #gets the frame
    #orangeLower=numpy.array([5, 50, 150], dtype="uint8") #uint8 necessary for this kind of thing
    #orangeUpper=numpy.array([100, 200, 255], dtype= "uint8") #represents upper and lower bounds of the color "orange"
    for col in colors: #iterating through each color
        minx, maxx, miny, maxy, output=largeRectangle(frame, col)
        #if a contour of the right color is detected...
        if(isinstance(minx, int) and maxx-minx>20):
            loadOverlayVideo(col)
            """if mode_select == 2:
                overlay_w = 40
                overlay_h = 30
            else:
                overlay_w = 64
                overlay_h = 64"""
            if count<stableTime:
                minxsum+=minx
                minysum+=miny
                maxxsum+=maxx
                maxysum+=maxy
                count+=1
            elif count==stableTime:
                #taking averages
                minxAverage=minxsum/stableTime
                minyAverage=minysum/stableTime
                maxxAverage=maxxsum/stableTime
                maxyAverage=maxysum/stableTime

                #resetting values
                minxsum=0
                maxxsum=0
                minysum=0
                maxysum=0
                count=0

                #the actual rectangle calculation
                cv2.rectangle(output, (minxAverage,minyAverage),(maxxAverage-minxAverage,maxyAverage-minyAverage),(0,255,0),2)
                centre_x = (maxxAverage + minxAverage)/2.0
                centre_y = (maxyAverage + minyAverage)/2.0
                print [centre_x, centre_y]
                playoverlay(centre_x - overlay_w / 2, centre_y - overlay_h / 2)

                print col
            if overlay_playing:
                overlayFrame(frame)
            break #so it doesn't cycle through all colors
            #rect = cv2.minAreaRect(contours)
            #box = cv2.boxPoints(rect)
            #box = np.int0(box)
            #cv2.drawContours(img,[box],0,(0,0,255),2)
            #ret, frame = cap.read()
            # Display the resulting frame
            #if overlay_playing:
                #overlayFrame(frame)
###Detection part


    cv2.imshow('cameraview', frame)
    # Display the resulting framegit pu
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
