import sys, subprocess, os
from moviepy.editor import VideoFileClip
import random

# we need to standardize all videos for grid making.
# so lets call the function from video_standardize.py

from video_standardize import standardize

# quick grids
cropped = []
concat_file = []

# ungraded person grid
def setup(input, output):
    # set user input as path
    path_cropped = input

    # create array of ungraded person
    for file in os.listdir(path_cropped):

        if file.endswith(".mp4"):

            # set append path to file
            file = path_cropped + "/" + file
            
            # append file to array as we're running a subprocess
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

        # create local variables
        # this is verbose, but avoiding an edge case.
        if grid_size == "6x4":
            ug1 = cropped[0]
            ug2 = cropped[1]
            ug3 = cropped[2]
            ug4 = cropped[3]
            ug5 = cropped[4]
            ug6 = cropped[5]
            ug7 = cropped[6]
            ug8 = cropped[7]
            ug9 = cropped[8]
            ug10 = cropped[9]
            ug11 = cropped[10]
            ug12 = cropped[11]
            ug13 = cropped[12]
            ug14 = cropped[13]
            ug15 = cropped[14]
            ug16 = cropped[15]
            ug17 = cropped[16]
            ug18 = cropped[17]
            ug19 = cropped[18]
            ug20 = cropped[19]
            ug21 = cropped[20]
            ug22 = cropped[21]
            ug23 = cropped[22]
            ug24 = cropped[23]

        elif grid_size == "7x5":
            ug1 = cropped[0]
            ug2 = cropped[1]
            ug3 = cropped[2]
            ug4 = cropped[3]
            ug5 = cropped[4]
            ug6 = cropped[5]
            ug7 = cropped[6]
            ug8 = cropped[7]
            ug9 = cropped[8]
            ug10 = cropped[9]
            ug11 = cropped[10]
            ug12 = cropped[11]
            ug13 = cropped[12]
            ug14 = cropped[13]
            ug15 = cropped[14]
            ug16 = cropped[15]
            ug17 = cropped[16]
            ug18 = cropped[17]
            ug19 = cropped[18]
            ug20 = cropped[19]
            ug21 = cropped[20]
            ug22 = cropped[21]
            ug23 = cropped[22]
            ug24 = cropped[23]
            ug25 = cropped[24]
            ug26 = cropped[25]
            ug27 = cropped[26]
            ug28 = cropped[27]
            ug29 = cropped[28]
            ug30 = cropped[29]
            ug31 = cropped[30]
            ug32 = cropped[31]
            ug33 = cropped[32]
            ug34 = cropped[33]
            ug35 = cropped[34]

        # no / improper grid size was caught in first conditional pass through.
        # for 8x5 grid
        else:
            ug1 = cropped[0]
            ug2 = cropped[1]
            ug3 = cropped[2]
            ug4 = cropped[3]
            ug5 = cropped[4]
            ug6 = cropped[5]
            ug7 = cropped[6]
            ug8 = cropped[7]
            ug9 = cropped[8]
            ug10 = cropped[9]
            ug11 = cropped[10]
            ug12 = cropped[11]
            ug13 = cropped[12]
            ug14 = cropped[13]
            ug15 = cropped[14]
            ug16 = cropped[15]
            ug17 = cropped[16]
            ug18 = cropped[17]
            ug19 = cropped[18]
            ug20 = cropped[19]
            ug21 = cropped[20]
            ug22 = cropped[21]
            ug23 = cropped[22]
            ug24 = cropped[23]
            ug25 = cropped[24]
            ug26 = cropped[25]
            ug27 = cropped[26]
            ug28 = cropped[27]
            ug29 = cropped[28]
            ug30 = cropped[29]
            ug31 = cropped[30]
            ug32 = cropped[31]
            ug33 = cropped[32]
            ug34 = cropped[33]
            ug35 = cropped[34]
            ug36 = cropped[35]
            ug37 = cropped[36]
            ug38 = cropped[37]
            ug39 = cropped[38]
            ug40 = cropped[39]

        # set ffmpeg command to create grids
        # if ffmpeg fails, instead of breaking the program..
        # mention standardization of videos, and to try again.
        
        if grid_size == "6x4":
            command_grid = "ffmpeg -i " + ug1 + " -i " + ug2 + " -i " + ug3 + " -i " + ug4 + " -i " + ug5 + " -i " + ug6 + " -i " + ug7 + " -i " + ug8 + " -i " + ug9 + " -i " + ug10 + " -i " + ug11 + " -i " + ug12 + " -i " + ug13 + " -i " + ug14 + " -i " + ug15 + " -i " + ug16 + " -i " + ug17 + " -i " + ug18 + " -i " + ug19 + " -i " + ug20 + " -i " + ug21 + " -i " + ug22 + " -i " + ug23 + " -i " + ug24 + " -filter_complex " + filer_complex + " -map " + map + " -crf 23 -preset veryfast -c:a copy " + "grid" + str(x) + ".mp4"
            try:
                subprocess.call(command_grid, shell=True)
            except:
                print("Please standardize your videos before generating grids.")
                print("Run perfectcrop -i [input] -t -o [output]")
                sys.exit(1)

        # for 7x5 grid
        elif grid_size == "7x5":
            command_grid = "ffmpeg -i " + ug1 + " -i " + ug2 + " -i " + ug3 + " -i " + ug4 + " -i " + ug5 + " -i " + ug6 + " -i " + ug7 + " -i " + ug8 + " -i " + ug9 + " -i " + ug10 + " -i " + ug11 + " -i " + ug12 + " -i " + ug13 + " -i " + ug14 + " -i " + ug15 + " -i " + ug16 + " -i " + ug17 + " -i " + ug18 + " -i " + ug19 + " -i " + ug20 + " -i " + ug21 + " -i " + ug22 + " -i " + ug23 + " -i " + ug24 + " -i " + ug25 + " -i " + ug26 + " -i " + ug27 + " -i " + ug28 + " -i " + ug29 + " -i " + ug30 + " -i " + ug31 + " -i " + ug32 + " -i " + ug33 + " -i " + ug34 + " -i " + ug35 + " -filter_complex " + filer_complex + " -map " + map + " -crf 23 -preset veryfast -c:a copy " + "grid" + str(x) + ".mp4"
            try:
                subprocess.call(command_grid, shell=True)
            except:
                print("Please standardize your videos before generating grids.")
                print("Run perfectcrop -i [input] -t -o [output]")
                sys.exit(1)
    
        # for 8x5 grid
        else:
            command_grid = "ffmpeg -i " + ug1 + " -i " + ug2 + " -i " + ug3 + " -i " + ug4 + " -i " + ug5 + " -i " + ug6 + " -i " + ug7 + " -i " + ug8 + " -i " + ug9 + " -i " + ug10 + " -i " + ug11 + " -i " + ug12 + " -i " + ug13 + " -i " + ug14 + " -i " + ug15 + " -i " + ug16 + " -i " + ug17 + " -i " + ug18 + " -i " + ug19 + " -i " + ug20 + " -i " + ug21 + " -i " + ug22 + " -i " + ug23 + " -i " + ug24 + " -i " + ug25 + " -i " + ug26 + " -i " + ug27 + " -i " + ug28 + " -i " + ug29 + " -i " + ug30 + " -i " + ug31 + " -i " + ug32 + " -i " + ug33 + " -i " + ug34 + " -i " + ug35 + "-i" + ug36 + "-i" + ug37 + "-i" + ug38 + "-i" + ug39 + "-i" + ug40 + " -filter_complex " + filer_complex + " -map " + map + " -crf 23 -preset veryfast -c:a copy " + "grid" + str(x) + ".mp4"
            try:
                subprocess.call(command_grid, shell=True)
            except:
                print("Please standardize your videos before generating grids.")
                print("Run perfectcrop -i [input] -t -o [output]")
                sys.exit(1)

    # create the output directory if it doesn't exist
    if not os.path.exists(output):
        os.makedirs(output)
    
    # move all grids to output directory
    for file in os.listdir("."):
        if file.endswith(".mp4") and file.startswith("grid"):
            os.rename(file, output + "/" + file)
    
    # enter output directory then run command_concat
    os.chdir(output)

    # create fl.txt with all the names of the files
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
