import sys, subprocess, os
from moviepy.editor import VideoFileClip
import random

# we need to standardize all videos for grid making.
# so lets call the function from video_standardize.py

from video_standardize import standardize
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# quick grids
cropped = []
concat_file = []

# ungraded person grid
def setup(input, output):
    # set user input as path
    path_cropped = input

    for file in os.listdir(path_cropped):

        if file.endswith(".mp4"):

            file = path_cropped + "/" + file
            cropped.append(file)

# print(ungraded_person)

def grid(input, output):

    grid_size = input("What grid size would you like to generate? (6x4, 7x5, 8x5): ")
    
    # map and mp1 never change, btw
    map = "[out_v]"
    map1 = "0:a"

    # set ffmpeg command 
    if grid_size == "6x4":
        filer_complex = "[1:v][0:v][3:v][2:v][4:v][5:v][6:v][7:v][8:v][9:v][10:v][11:v][12:v][13:v][14:v][15:v][16:v][17:v][18:v][19:v][20:v][21:v][22:v][23:v]xstack=inputs=24:grid=6x4:shortest=true[out_v]"
    elif grid_size == "7x5":
        filer_complex = "[1:v][0:v][3:v][2:v][4:v][5:v][6:v][7:v][8:v][9:v][10:v][11:v][12:v][13:v][14:v][15:v][16:v][17:v][18:v][19:v][20:v][21:v][22:v][23:v][24:v][25:v][26:v][27:v][28:v][29:v][30:v][31:v][32:v][33:v][34:v]xstack=inputs=35:grid=7x5:shortest=true[out_v]"
    elif grid_size == "8x5":
        filer_complex = "[1:v][0:v][3:v][2:v][4:v][5:v][6:v][7:v][8:v][9:v][10:v][11:v][12:v][13:v][14:v][15:v][16:v][17:v][18:v][19:v][20:v][21:v][22:v][23:v][24:v][25:v][26:v][27:v][28:v][29:v][30:v][31:v][32:v][33:v][34:v][35:v][36:v][37:v][38:v][39:v]xstack=inputs=40:grid=8x5:shortest=true[out_v]"
    else:
        print("Please enter a valid grid size.")
        sys.exit(1)

    # set grid generate limit.. will generate x amounts of grids
    gen_limit = 400

    # run loop to create grid_generate_limit amount of grids.
    x = 0
    for y in range(0, gen_limit):

        # count iteration
        x += 1

        # shuffle every loop
        random.shuffle(cropped)

        if grid_size == "6x4":
            ug = cropped[:24]
            ug1, ug2, ug3, ug4, ug5, ug6, ug7, ug8, ug9, ug10, ug11, ug12, ug13, ug14, ug15, ug16, ug17, ug18, ug19, ug20, ug21, ug22, ug23, ug24 = ug

        elif grid_size == "7x5":
            ug = cropped[:35]
            ug1, ug2, ug3, ug4, ug5, ug6, ug7, ug8, ug9, ug10, ug11, ug12, ug13, ug14, ug15, ug16, ug17, ug18, ug19, ug20, ug21, ug22, ug23, ug24, ug25, ug26, ug27, ug28, ug29, ug30, ug31, ug32, ug33, ug34, ug35 = ug

        else:
            ug = cropped[:40]
            ug1, ug2, ug3, ug4, ug5, ug6, ug7, ug8, ug9, ug10, ug11, ug12, ug13, ug14, ug15, ug16, ug17, ug18, ug19, ug20, ug21, ug22, ug23, ug24, ug25, ug26, ug27, ug28, ug29, ug30, ug31, ug32, ug33, ug34, ug35, ug36, ug37, ug38, ug39, ug40 = ug

        # set ffmpeg command to create grids
        # if ffmpeg fails, instead of breaking the program..
        # mention standardization of videos, and to try again.
        
        if grid_size == "6x4":
            command_grid = f"ffmpeg {' '.join(['-i ' + ug for ug in cropped[:24]])} -filter_complex {filer_complex} -map {map} -crf 23 -preset veryfast -c:a copy grid{x}.mp4"
        elif grid_size == "7x5":
            command_grid = f"ffmpeg {' '.join(['-i ' + ug for ug in cropped[:35]])} -filter_complex {filer_complex} -map {map} -crf 23 -preset veryfast -c:a copy grid{x}.mp4"
        elif grid_size == "8x5":
            command_grid = f"ffmpeg {' '.join(['-i ' + ug for ug in cropped[:40]])} -filter_complex {filer_complex} -map {map} -crf 23 -preset veryfast -c:a copy grid{x}.mp4"
        else:
            print("Please enter a valid grid size.")
            sys.exit(1)

        try:
            subprocess.call(command_grid, shell=True)
        except:
            logger.error("Please standardize your videos before generating grids.")
            logger.error("Run perfectcrop -i [input] -t -o [output]")
            sys.exit(1)

    if not os.path.exists(output):
        os.makedirs(output)
    
    for file in os.listdir("."):
        if file.endswith(".mp4") and file.startswith("grid"):
            os.rename(file, output + "/" + file)
    
    os.chdir(output)

    command_fl = "find *.mp4 | sed 's:\ :\\\ :g'| sed 's/^/file /' > fl.txt"
    command_concat = "for file in *.mp4; do ffmpeg -f concat -i fl.txt -c copy output.mp4; rm fl.txt"
    try:
        subprocess.call(command_fl, shell=True)
        subprocess.call(command_concat, shell=True)
    except:
        print("Please standardize your videos before concatenating.")
        print("Run perfectcrop -i [input] -t -o [output]")
        sys.exit(1)

if __name__ == "__main__":
    setup(input, output)
    grid(input, output)
