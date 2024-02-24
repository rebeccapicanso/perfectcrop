from moviepy.editor import VideoFileClip, concatenate_videoclips
from shots import get_shots
import random

VIDEO = "myvideo.mp4"

# get the start and end times in a video
scenes = get_shots(VIDEO)

vidfile = VideoFileClip(VIDEO)

# naming count, replace w whatever
count = 0

# creating a method just so we can import as a module.........
# this will create a subclip for each scene and writes the video file

def splice():

    for s in scenes:
        count +1
        clip = vidfile.subclip(s["start"], s["end"])
        clip.write_videofile(f'{count}_detected')

splice()
