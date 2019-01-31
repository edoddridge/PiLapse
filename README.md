# PiLapse
Time lapse photography with a Raspberry Pi

# Make a movie
To turn the series of jpg files into a movie with `ffmpeg`

`ffmpeg -r 10 -start_number 23 -i image%6d.jpg  -b:v 40M -vf eq=brightness=0.08 -r 30 video.avi`

Or, with motion interpolation to smooth the footage:

`ffmpeg -r 10 -start_number 23 -i image%6d.jpg  -filter:v minterpolate -b:v 40M -vf eq=brightness=0.08 -r 30 video.avi`
