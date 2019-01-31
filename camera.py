#!/usr/bin/python3

print(" ")
print("**************************************************")
print("*   Running timelapse script in the background   *")

from cam_utils import working_directory, make_dir
from picamera import PiCamera
from time import sleep
import datetime
import os
import glob

now = datetime.datetime.now()
now_string = now.strftime("%Y-%m-%d-%H%M")


print("*    timelapse started at {0}        *".format(now_string))
print("**************************************************")
print(" ")

path = '/home/pi/Documents/bike-lapse/'

picture_dir = path + now_string
# use iterative function to avoid duplicate diectories
picture_dir = make_dir(picture_dir)

camera = PiCamera()
camera.resolution = (3280, 2464)
camera.rotation = (270)
camera.meter_mode = 'matrix'
delay = 1

with working_directory(picture_dir):
    for i, filename in enumerate(camera.capture_continuous('image{counter:06d}.jpg')):
        sleep(delay)
        if i == 2:
            break

