# Standardize all videos for grid making.
# As this is dependant on bash scripts via ffmpeg, source videos are a little tricky to delete. Please use proper file management.

import subprocess
import os

def standardize(videofile):
    command_shorten = 'for file in *.mp4; do ffmpeg -ss 00:00:00.00 -i in.mp4 -t 2 -map 0 working/${file} ; done'
    command_codecs = 'for file in *.mp4; do ffmpeg -i ${file} -c:v libx264 -crf 23 -preset veryfast -c:a copy working/${file}.mp4; done'
    subprocess.call(command_shorten, command_codecs)

  
# shorten all videos to 2 seconds
# for file in *.mp4; do ffmpeg -ss 00:00:00.00 -i in.mp4 -t 2 -map 0 test_dump/${file} ; done

# concatenate & standardize to shortest video, audio.
# ffmpeg -y -f s16be -i /dev/zero -af "[in]anullsink;amovie=1.wav[a1];amovie=silence.wav[a2];amovie=2.wav[a3];amovie=4.wav[a4];[a1][a2][a3][a4]concat=n=4:v=0:a=1[out]" -shortest -t 12 output.wav

# concatenate all files in a directory together by creating a text file with names of files and then reading from it.
# find *.mp4 | sed 's:\ :\\\ :g'| sed 's/^/file /' > fl.txt; ffmpeg -f concat -i fl.txt -c copy output.mp4; rm fl.txt

# standardize video codecs to avoid flip glitching
# ffmpeg -i ${file} -c:v libx264 -crf 23 -preset veryfast -c:a copy ${file}.mp4

