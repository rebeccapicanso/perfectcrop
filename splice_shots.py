from moviepy.editor import VideoFileClip, concatenate_videoclips
from shots import get_shots
import random

VIDEO = "myvideo.mp4"

# get the start and end times in a video
scenes = get_shots(VIDEO)

vidfile = VideoFileClip(VIDEO)

# naming count, replace w whatever
count = 0

# create a subclip for each scene and add to the clips list
for s in scenes:
    count +1
    clip = vidfile.subclip(s["start"], s["end"])
    clip.write_videofile(f'{count}_detected')

# randomize the order of the clips
random.shuffle(clips)

# save a video
composition = concatenate_videoclips(clips)
composition.write_videofile("randomized.mp4")
