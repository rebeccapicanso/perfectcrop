import argparse
import sys
import grid
import shots
import video_standardize
import perfect_crop


def main():
    """
    Run the command line version of Perfect Crop.
    """

    parser = argparse.ArgumentParser(
        add_help=False,
        description="Perfect Crop is a tool to crop videos to a specific object in the video.")

    parser.add_argument(
        "-i",
        "--input",
        help="The input video file or directory of video files to process.",
        action="store",
        required=True,
        dest="input")

    # just use boolean logic for arguments
    parser.add_argument(
        "-s",
        "--shots",
        dest="shots",
        default="False",
        help="Run the shots function.",
        action="store_true")
    
    parser.add_argument(
        "-g",
        "--grid",
        help="Run the grid function.",
        dest= "grid",
        default="False",
        action="store_true")
    
    parser.add_argument(
        "-p",
        "--perfect_crop",
        help="Run the perfect crop function.",
        dest="perf",
        default="False",
        action="store_true")
    
    parser.add_argument(
        "-t",
        "--standardize",
        dest="standardize",
        help="Run the standardize function.",
        default="False",
        action="store_true")
    
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        # if no output is given, set it to the current directory
        default=".",
        action="store",
        required=True,
        help="The output directory to save the processed videos.")

    args = parser.parse_args()

    # this isn't totally necessary, but again avoiding an edge case.
    perfcrop = args.perf
    shots_ = args.shots
    grid_ = args.grid
    standardize_ = args.standardize

    if perfcrop == True:
        perfect_crop.save_images(args.input, args.output)
    elif shots_ == True:
        shots.get_shots(args.input, args.output)
    elif standardize_ == True:
        video_standardize(args.input, args.output)
    elif grid_ == True:
        grid(args.input, args.output)
    else:
        print("Please specify a function to run.")
        sys.exit(1)

if __name__ == "__main__":
    main()
