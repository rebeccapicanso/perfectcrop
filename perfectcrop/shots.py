import json
import os
from moviepy.editor import VideoFileClip
from scenedetect import ContentDetector, detect


def get_shots(video):

    print("Finding shots in", video) 

    outname = video + ".shots.json"

    vidfile = VideoFileClip(video)

    if os.path.exists(outname):
        with open(outname, "r") as infile:
            return json.load(infile)

    shots = []
    count = 0
    scene_list = detect(video, ContentDetector())

    # make directory in path for clips
    if not os.path.exists("clips"):
        os.makedirs("clips")
        
    # comment me out if you only want to generate a .json file with shot indexing
    for shot in scene_list:
        item = {
            "start": shot[0].get_seconds(),
            "end": shot[1].get_seconds(),
        }
        shots.append(item)
        count += 1

        # create separate clip

        clip = vidfile.subclip(item["start"], item["end"])
        
        # due to the nature of moviepy, the clip will always include the original file name
        # these clips are ultimately placeholders.

        clipname = count + ".mp4"
        clip.write_videofile(f'{clipname}')
    
    with open(outname, "w") as outfile:
        json.dump(shots, outfile, indent=2)

    return shots
