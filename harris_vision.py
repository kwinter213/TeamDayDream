# Fork #1 - Harris Corner Detection Method
# Anderson
# Softdes Final Project

## Post notes - able to select corners, but formation of a bounding box is
## difficult due to polylines
## It is also not possible to identify objects by their edge signatures

import cv2
import numpy as np

filename = 'sample2.jpg'
img = cv2.imread(filename)
# creates grey image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
cv2.imwrite('output.png',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
