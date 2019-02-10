#!/usr/bin/python3

from cam_utils import working_directory, make_dir
from picamera import PiCamera
from time import sleep
import datetime
import os
import glob

def run_timelapse():
    """Start taking a timelapse."""

    print(" ")
    print("**************************************************")
    print("*   Running timelapse script in the background   *")

    now = datetime.datetime.now()
    now_string = now.strftime("%Y-%m-%d-%H%M")

    print("*    timelapse started at {0}        *".format(now_string))
    print("**************************************************")
    print(" ")

    path = '/home/pi/Documents/bike-lapse/'

    picture_dir = path + now_string
    # use iterative function to avoid duplicate diectories
    # this is important if the RPi doesn't keep time properly
    picture_dir = make_dir(picture_dir)

    camera = PiCamera()
    # 2x2 binned (2 megapixels)
    # camera.resolution = (1640, 1232)
    # full resolution (8 megapixels)
    camera.resolution = (3280, 2464)
    camera.rotation = (270)
    camera.meter_mode = 'spot'#'matrix'
    # minimum time between images in seconds
    delay = 0.25

    # pause to allow me to get bike sorted out
    sleep(15)

    with working_directory(picture_dir):
        for i, filename in enumerate(camera.capture_continuous('image{counter:06d}.jpg')):
            sleep(delay)
    #        if i == 2:
    #            break

if __name__ == '__main__':
    run_timelapse()
