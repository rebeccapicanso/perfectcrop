import argparse
from . import grid, perfect_crop, shots, video_standardize

#   -p   [video or directory]    | crop a video or directory of clips to select label (runs perfect_crop.py)

#   -s   [video]                 | create .json file identifying shots (scene changes) in a long form video. shots.py will then splice the video into individual clips (or scenes).
  
#   -vs  [video or directory]    | standardizes video length, codecs, etc. with ffmpeg bash. needed for concatenation!
  
#   -g   [video or directory]    | creates a dynamic, randomized moving video grid with ffmpeg bash commands. this is a legacy file from Court Laureate, not necessary for the project itself :)

#   -l   [video or directory]    | for a select object, identifies what shots that label appears, and then records the average location of that object.

def main():
    parser = argparse.ArgumentParser(description="Perfect Crop is a tool to crop videos to a specific object in the video.")
    parser.add_argument("-p", "--perfect_crop", help="crop a video or directory of clips to select label", nargs=2, metavar=("label", "video"))
    parser.add_argument("-s", "--shots", help="create .json file identifying shots (scene changes) in a long form video. shots.py will then splice the video into individual clips (or scenes).", metavar="video")
    parser.add_argument("-vs", "--video_standardize", help="standardizes video length, codecs, etc. with ffmpeg bash. needed for concatenation!", metavar="video")
    parser.add_argument("-g", "--grid", help="creates a dynamic, randomized moving video grid with ffmpeg bash commands. this is a legacy file from Court Laureate, not necessary for the project itself :)", metavar="video")
    parser.add_argument("-l", "--label", help="for a select object, identifies what shots that label appears, and then records the average location of that object.", metavar="video")
    args = parser.parse_args()

    if args.perfect_crop:
        perfect_crop.save_images(args.perfect_crop[1], args.perfect_crop[0])
        perfect_crop.average_crop(args.perfect_crop[1], perfect_crop.average_center)
    elif args.shots:
        shots.shots(args.shots)
    elif args.video_standardize:
        video_standardize.standardize(args.video_standardize)
    elif args.grid:
        grid.nightmare_grid(args.grid)
    elif args.label:
        perfect_crop.save_images(args.label[1], args.label[0])
        perfect_crop.average_crop(args.label[1], perfect_crop.average_center)
    else:
        print("Please use the correct flags to run Perfect Crop.")
        print("-p flag for perfect crop, followed by label flag, followed by video file")
        print("-s flag for shots, followed by video file")
        print("-vs flag for video standardize, followed by video file")
        print("-g flag for nightmare grid, followed by video file")
