# Standardize all videos for grid making.
# As this is dependant on bash scripts via ffmpeg, source videos are a little tricky to delete. Please use proper file management.

import subprocess
import os
import sys

def standardize(input, output):
    # set user input as video length
    video_length = input("How long would you like the videos to be? (in seconds): ")

    # and then create a command to shorten the videos
    command_shorten = f'for file in *.mp4; do ffmpeg -ss 00:00:00.00 -i in.mp4 -t {video_length} -map 0 working/${file} ; done'
    command_codecs = 'for file in *.mp4; do ffmpeg -i ${file} -c:v libx264 -crf 23 -preset veryfast -c:a copy working/${file}.mp4; done'
    
    # now to test
    try:
        subprocess.call(command_shorten, command_codecs)
    except:
        print("Something's wrong with your videos. Check & try again.")
        print("Maybe permissions?")
        sys.exit(1)

    # create the output directory if it doesn't exist
    if not os.path.exists(output):
        os.makedirs(output)
    
    # move all files to output directory
    for file in os.listdir("working"):
        if file.endswith(".mp4") != input:
            os.rename(file, output + "/" + file)
    
    # notify file location
    print("Files are in", output)

if __name__ == "__main__":
    standardize()
    
