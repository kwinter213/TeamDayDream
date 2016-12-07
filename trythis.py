import cv2
import time

MAXFRAMES=60
OVERLAYFRAMERATE = 12
fc_overlay = 0  # frame count of overlay video
video_overlay=[]
overlay_x = 250
overlay_y = 200
overlay_w = 40
overlay_h = 30
overlay_starttime = 0
overlay_playing = True

def loadOverlayVideo():
    """
    Load and generate overlay video, It's just for demo
    """
    global video_overlay, fc_overlay
    fc_overlay = MAXFRAMES
    video_overlay = []
    for i in range(fc_overlay):
        video_overlay.append(cv2.imread('video/' + str(i) + '.png'))

def playoverlay(x, y):
    global overlay_playing, overlay_starttime, overlay_x, overlay_y
    overlay_playing = True
    overlay_starttime = time.clock()
    overlay_x = x
    overlay_y = y

def click(event, x, y, flags, param):
    # if the left mouse button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        playoverlay(x, y)

def overlayFrame(frame):
    global overlay_playing
    # get frame number of overlay frame
    currTime = time.clock() - overlay_starttime
    if currTime > MAXFRAMES / OVERLAYFRAMERATE:
        overlay_playing = False
    frame_no = int(currTime * OVERLAYFRAMERATE) % fc_overlay
    # composite overlay frame
    frame[overlay_y : overlay_y + overlay_h, overlay_x : overlay_x + overlay_w] = video_overlay[frame_no]

cap = cv2.VideoCapture(0)
cv2.namedWindow('cameraview')
cv2.setMouseCallback('cameraview', click)

loadOverlayVideo()

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    if overlay_playing:
        overlayFrame(frame)

    cv2.imshow('cameraview', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
