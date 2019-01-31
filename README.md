# PiLapse
Time lapse photography with a Raspberry Pi

# To run on boot
To make the script run with standard user privileges when the Raspberry Pi boots up, add the following as the final line of `~/.bashrc`

`python3 /home/pi/Documents/bike-lapse/camera.py >> /home/pi/Documents/bike-lapse/log.txt 2>&1 &`

There are other options, but they run the script as root, which means you need to use `sudo` all the time when dealing with the files :(

# Make a movie
To turn the series of jpg files into a movie with `ffmpeg`

`ffmpeg -r 10 -start_number 23 -i image%6d.jpg  -b:v 40M -vf eq=brightness=0.08 -r 30 video.avi`

Or, with motion interpolation to smooth the footage:

`ffmpeg -r 10 -start_number 23 -i image%6d.jpg  -filter:v minterpolate -b:v 40M -vf eq=brightness=0.08 -r 30 video.avi`
