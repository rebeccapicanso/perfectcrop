import argparse
from . import grid, perfect_crop, shots, video_standardize

def main():
    """
    Run the command line version of Perfect Crop
    """
    parser = argparse.ArgumentParser(
        description="Perfect Crop is a tool to crop videos to a specific object in the video."
    )
    parser.add_argument(
        "--input",
        "-i",
        help="The input video file or directory of video files to process.",
        nargs="*",
        required=True,
        dest="input")

    parser.add_argument(
        "-p",
        "--perfectcrop",
        dest="perfectcrop",
        action="append",
        help="Crop a video or directory of clips to select label (runs perfect_crop.py)"
        )
    
    # label used for object detection
    parser.add_argument(
        "-l",
        "--label",
        dest="label",
        action="append",
        help="Label used for object detection with perfect_crop.py"
    )

    parser.add_argument(
        "-s", 
        "--shots",
        dest="shots",
        action="append",
        help="Create .json file identifying shots (scene changes) in a long form video. shots.py will then splice the video into individual clips (or scenes)."
        )
    parser.add_argument(
        "-vs", 
        "--standardize",
        dest="standardize",
        action="append",
        help="Standardizes video length, codecs, etc. with ffmpeg bash. needed for concatenation!")
    
    parser.add_argument(
        "-g", 
        "--grid",
        dest="grid",
        action="append",
        help="Creates a dynamic, randomized moving video grid with ffmpeg bash commands. this is a legacy file from Court Laureate, not necessary for the project itself :)")

    parser.add_argument(
        "-h",
        "--help",
        action="help",
        help="Show this help message and exit."
    )

    args = parser.parse_args()
    print(args)

    if args.perfectcrop:
        perfect_crop.save_images(args.input, args.label)
        perfect_crop.average_center(args.input)

    if args.shots:
        shots(args.input)

    if args.standardize:
        video_standardize(args.input)
    
    if args.grid:
        print("please note that the input must be a directory of clips, not a single file.")
        grid(args.input)

    if args.help:
        print("Perfect Crop is a tool to crop videos to a specific object in the video.\n" +
              "Usage: perfectcrop -i [INPUT] [OPTIONS]" )
    
    else:
        print("No tasks specified. Please run -h or --help for more information.")


if __name__ == "__main__":
    main()
