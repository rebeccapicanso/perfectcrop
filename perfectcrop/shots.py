import json
import os
from moviepy.editor import VideoFileClip
from scenedetect import ContentDetector, detect


def get_shots(input, output):

    print("Finding shots in", input) 

    outname = input + ".shots.json"

    vidfile = VideoFileClip(input)

    if os.path.exists(outname):
        with open(outname, "r") as infile:
            return json.load(infile)

    shots = []
    count = 0
    scene_list = detect(input, ContentDetector())
        
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
        
        clipname = f'{count}' + ".mp4"
        clip.write_videofile(f'{clipname}')
    
    # after all the spliced clips render, we move them to the output directory, excluding the input clip.
    if not os.path.exists(f'{output}'):
        os.makedirs(f'{output}')
    
    os.system(f'mv *.mp4 {output}')
    os.system(f'mv {output}/{input} .')

    # notify file location
    print("Files are in " + output)
    print("To run again, you'll need to delete the .json file.")
        
    # then we .json dump
    with open(outname, "w") as outfile:
        json.dump(shots, outfile, indent=2)

    return shots

# when shots is called in cli.py, run get_shots
if __name__ == "__main__":
    # set up get_shots to recieve two arguments from cli.py
    get_shots(input, output)
