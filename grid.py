import sys, subprocess, os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import random

# please run 'ulimit -n' in terminal to see your current limit
# then run 'ulimit -n 2048' to increase the limit to 2048
# please keep in mind that this is isolated to the terminal window & you will need to reset

# quick grids

ungraded_person = []
concat_file = []

# ungraded person grid
def setup(path):
    # set user input as path
    path_ungraded_person = path

    # create array of ungraded person
    for file in os.listdir(path_ungraded_person):

        if file.endswith(".mp4"):
            # set append path to file

            file = path_ungraded_person + "/" + file
            # append file to array

            ungraded_person.append(file)

            # composition = concatenate_videoclips(ungraded_person)
            # composition.write_videofile("opening4.mp4")

# print(ungraded_person)

def grid(ungraded_person):
    # set ffmpeg command 
    # 8x5 grid
    # filer_complex = "[1:v][0:v][3:v][2:v][4:v][5:v][6:v][7:v][8:v][9:v][10:v][11:v][12:v][13:v][14:v][15:v][16:v][17:v][18:v][19:v][20:v][21:v][22:v][23:v][24:v][25:v][26:v][27:v][28:v][29:v][30:v][31:v][32:v][33:v][34:v][35:v][36:v][37:v][38:v][39:v]xstack=inputs=40:grid=8x5:shortest=true[out_v]"
    # 7x5 grid
    # filer_complex = "[1:v][0:v][3:v][2:v][4:v][5:v][6:v][7:v][8:v][9:v][10:v][11:v][12:v][13:v][14:v][15:v][16:v][17:v][18:v][19:v][20:v][21:v][22:v][23:v][24:v][25:v][26:v][27:v][28:v][29:v][30:v][31:v][32:v][33:v][34:v]xstack=inputs=35:grid=7x5:shortest=true[out_v]"
    # 6x4 grid
    filer_complex = "[1:v][0:v][3:v][2:v][4:v][5:v][6:v][7:v][8:v][9:v][10:v][11:v][12:v][13:v][14:v][15:v][16:v][17:v][18:v][19:v][20:v][21:v][22:v][23:v]xstack=inputs=24:grid=6x4:shortest=true[out_v]"
    map = "[out_v]"
    map1 = "0:a"

    # set grid generate limit.. will generate x amounts of grids
    grid_generate_limit = 400

    # set static limit
    static = []

    # set ungraded person limit.. either 24 or 35 for 6x4 or 7x5 respectively
    # ug_limit = 35

    # run loop to create grid_generate_limit amount of grids
    x = 0
    for y in range(0, 300):
        # count iteration
        x += 1

        # shuffle every loop
        random.shuffle(ungraded_person)
        # create local variables
        ug1 = ungraded_person[0]
        ug2 = ungraded_person[1]
        ug3 = ungraded_person[2]
        ug4 = ungraded_person[3]
        ug5 = ungraded_person[4]
        ug6 = ungraded_person[5]
        ug7 = ungraded_person[6]
        ug8 = ungraded_person[7]
        ug9 = ungraded_person[8]
        ug10 = ungraded_person[9]
        ug11 = ungraded_person[10]
        ug12 = ungraded_person[11]
        ug13 = ungraded_person[12]
        ug14 = ungraded_person[13]
        ug15 = ungraded_person[14]
        ug16 = ungraded_person[15]
        ug17 = ungraded_person[16]
        ug18 = ungraded_person[17]
        ug19 = ungraded_person[18]
        ug20 = ungraded_person[19]
        ug21 = ungraded_person[20]
        ug22 = ungraded_person[21]
        ug23 = ungraded_person[22]
        ug24 = ungraded_person[23]

        # comment out below if only creating a 6x4 grid
        # this makes it 7x5!!!

        ug25 = ungraded_person[24]
        # ug26 = ungraded_person[25]
        # ug27 = ungraded_person[26]
        # ug28 = ungraded_person[27]
        # ug29 = ungraded_person[28]
        # ug30 = ungraded_person[29]
        # ug31 = ungraded_person[30]
        # ug32 = ungraded_person[31]
        # ug33 = ungraded_person[32]
        # ug34 = ungraded_person[33]
        # ug35 = ungraded_person[34]

        # comment out below if only creating a 7x5 grid
        # this makes it 8x5!!!

        # ug36 = ungraded_person[35]
        # ug37 = ungraded_person[36]
        # ug38 = ungraded_person[37]
        # ug39 = ungraded_person[38]
        # ug40 = ungraded_person[39]

        # create static
        # static_placeholder = 0



# for additional grid shapes, uses..

#         # clip = VideoFileClip(ungraded_person[1])
#         # clip = clip.crop(x1=1000, width=32)
#         # clip.write_videofile(ungraded_person[1]+"thin_.mp4")
#         # bulk crop

#         # # iterate 24 times
#         # for i in range(0, 23):
#         #     # set clip
#         #     clip = VideoFileClip(ungraded_person[i])
#         #     # crop clip
#         #     clip = clip.crop(clip, x1=100, width=5)
#         #     # save clip
#         #     clip.write_videofile(ungraded_person[i]+"thin_.mp4")


        # set ffmpeg command

        command = "ffmpeg -i " + ug1 + " -i " + ug2 + " -i " + ug3 + " -i " + ug4 + " -i " + ug5 + " -i " + ug6 + " -i " + ug7 + " -i " + ug8 + " -i " + ug9 + " -i " + ug10 + " -i " + ug11 + " -i " + ug12 + " -i " + ug13 + " -i " + ug14 + " -i " + ug15 + " -i " + ug16 + " -i " + ug17 + " -i " + ug18 + " -i " + ug19 + " -i " + ug20 + " -i " + ug21 + " -i " + ug22 + " -i " + ug23 + " -i " + ug24 + " -filter_complex " + filer_complex + " -map " + map + " -crf 23 -preset veryfast -c:a copy " + "grid" + str(x) + ".mp4"

        # command = "ffmpeg -i " + ug1 + " -i " + ug2 + " -i " + ug3 + " -i " + ug4 + " -i " + ug5 + " -i " + ug6 + " -i " + ug7 + " -i " + ug8 + " -i " + ug9 + " -i " + ug10 + " -i " + ug11 + " -i " + ug12 + " -filter_complex " + filer_complex + " -map " + map + " -map " + map1 + " -c:v libx264 -crf 23 -preset veryfast -c:a copy " + "grid" + str(x) + ".mp4"
        concat_file = "grida" + str(x) + "a.mp4"
        # run command
        subprocess.call(command, shell=True)

# # for some reason this below doesn't work yet

# # STANDARDIZE
# # ffmpeg -i ${file} -c:v libx264 -crf 23 -preset veryfast -c:a copy ${file}.mp4

# # SHORTEN
# # ffmpeg -i movie.mp4 -ss 00:00:00 -t 00:00:01 -async 1 -strict -2 cut.mp4 

# # CONCATENATE
# # find *.mp4 | sed 's:\ :\\\ :g'| sed 's/^/file /' > fl.txt; ffmpeg -f concat -i fl.txt -c copy output.mp4; rm fl.txt

# # BLUE HUE
# # ffmpeg -i punch.mp4 -filter_complex "[0:v]pixelize,colorize=hue=197.29:saturation=0.7:lightness=0.5[out_v]" -map "[out_v]" out.mp4


# # accept user input to set path in main
if __name__ == "__main__":
    import sys
    for f in sys.argv[1:]:
        setup(f)
        grid(ungraded_person)
        # concat(concat_file, f)



# note! you will run into a "too many files open error"


# ffmpeg -y -f s16be -i /dev/zero -af "[in]anullsink;amovie=1.wav[a1];amovie=silence.wav[a2];amovie=2.wav[a3];amovie=4.wav[a4];[a1][a2][a3][a4]concat=n=4:v=0:a=1[out]" -shortest -t 12 output.wav


