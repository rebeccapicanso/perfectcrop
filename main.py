# main.py magic
# unfinished, looking to publish sometime before the weekend.

import subprocess
import os
import perfect_crop
import moving_crop
import shots
import splice_shots
import video_standardize
import grid



if __name__ == "__main__":
    import sys

    # -p flag for perfect crop, followed by label flag, followed by video file
    # -s flag for shots, followed by video file
    # -vs flag for video standardize, followed by video file
    # -g flag for grid, followed by video file

    if sys.argv[1] == "-p":
        perfect_crop.save_images(sys.argv[3], sys.argv[2])
        perfect_crop.average_crop(sys.argv[3], perfect_crop.average_center)
    elif sys.argv[1] == "-s":
        shots.shots(sys.argv[2])
    elif sys.argv[1] == "-vs":
        video_standardize.standardize(sys.argv[2])
    elif sys.argv[1] == "-ng":
        nightmare_grid.nightmare_grid(sys.argv[2])
    elif sys.argv[1] == "-help":
        print("Perfect Crop is a tool to crop videos to a specific object in the video.")
        print("Use the -p flag for perfect crop, followed by label flag, followed by video file")
        print("Use the -s flag for shots, followed by video file")
        print("Use the -vs flag for video standardize, followed by video file")
        print("Use the -ng flag for nightmare grid, followed by video file")
    else:
        print("Please use the correct flags to run Perfect Crop.")
        print("-p flag for perfect crop, followed by label flag, followed by video file")
        print("-s flag for shots, followed by video file")
        print("-vs flag for video standardize, followed by video file")
        print("-ng flag for nightmare grid, followed by video file")

