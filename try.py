import cv2
import time

MAXFRAMES=60    # max number of frames (length of animation)
NUM_FRAMES=24   # number of animation frames
OVERLAYFRAMERATE = 24
fc_overlay = 0  # frame count of overlay video
video_overlay=[]
overlay_x = 0
overlay_y = 0
overlay_w = 64
overlay_h = 64
overlay_starttime = 0
overlay_playing = False
size = (32,32)

def loadOverlayVideo():
    """
    Load and generate overlay video, It's just for demo
    """
    global video_overlay, size
    video_overlay = []
    for i in range(NUM_FRAMES):
        # load 4-channel png image
        video_overlay.append(cv2.imread('video_1/ani-' + str(i) + '.png', cv2.IMREAD_UNCHANGED))

def playoverlay(x, y):
    global overlay_playing, overlay_starttime, overlay_x, overlay_y
    overlay_playing = True
    overlay_starttime = time.clock()
    overlay_x = x
    overlay_y = y

def click(event, x, y, flags, param):
    # if the left mouse button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        playoverlay(x - overlay_w / 2, y - overlay_h / 2)

def overlayFrame(frame):
    global overlay_playing
    # get frame number of overlay frame
    currTime = time.clock() - overlay_starttime
    if currTime > MAXFRAMES / OVERLAYFRAMERATE:
        overlay_playing = False
    frame_no = int(currTime * OVERLAYFRAMERATE) % NUM_FRAMES
    # composite overlay frame
    for c in range(0,3):
        alpha = video_overlay[frame_no][:,:, 3] / 255.0
        color = video_overlay[frame_no][:,:, c] * (alpha)
        beta  = frame[overlay_y : overlay_y + overlay_h, overlay_x : overlay_x + overlay_w, c] * (1.0 - alpha)
        frame[overlay_y : overlay_y + overlay_h, overlay_x : overlay_x + overlay_w, c] = color + beta

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
