# Blob Detection V1.1
# To be added:
# - White BG auto calibration
# - Enrollment of all colors

import time
import sys
import numpy as np
import SimpleCV

from settings import *

vs = SimpleCV.VideoStream("test.avi")

def dist_from_color(img, color):
    '''
    SimpleCV.Image, tuple -> int
    tuple: (r, g, b)
    '''

    # BUG in getNumpy, it returns with colors reversed
    matrix = (img.getNumpy()[:, :, [2, 1, 0]] - color) ** 2
    width, height = img.size()
    return matrix.sum() ** 0.5 / (width * height)


def main():

    print(__doc__)
    cam = SimpleCV.Camera(camera_index=-1)
    display = False
    if len(sys.argv) > 1:
        display = sys.argv[1]

    # wait some time for the camera to turn on
    time.sleep(1)
    background = cam.getImage()

    print('Everything is ready. Starting to track!')

    while True:

        img = cam.getImage()
        dist = ((img - background) + (background - img)).dilate(5)
        # segmented = dist
        segmented = dist.binarize(COLOR_BINARIZATION_THRESHOLD).invert()
        blobs = segmented.findBlobs(minsize=ITEM_DIMENSION ** 2)
        if blobs:
            points = []
            for b in blobs:
                points.append((b.x, b.y))
                car = img.crop(b.x, b.y,
                               ITEM_DIMENSION, ITEM_DIMENSION, centered=True)
                # color distances from items
                dists = [dist_from_color(car, c['color']) for c in ITEMS]
                chosen_items = ITEMS[np.argmin(dists)]['name']
                print(b.x, b.y, chosen_items)

        if display:
            to_show = locals()[display]
            if blobs:
                to_show.drawPoints(points)
            to_show.show()
            to_show.save(vs)
        else:
            time.sleep(0.1)


if __name__ == '__main__':
    main()
