# perfect crop

Perfect Crop will locate a detected object within a video clip, find its average location, and create a cropped clip from the center.

for example, searching the video for "cell phone":
Source Clip            |  Detected Object
:-------------------------:|:-------------------------:
![](https://github.com/rebeccapicanso/perfect_crop/blob/main/readme_source.gif)| ![](https://github.com/rebeccapicanso/perfect_crop/blob/main/readme_detected.gif)

Perfect Crop can also index a video & splice into individual scenes without quality loss.

```
perfectcrop accepts the following inputs:

  -p   [video, directory]    | crop a video or directory of clips to select label (runs perfect_crop.py)

  -s   [video]               | create .json file identifying shots (scene changes) in a long form video. shots.py will then splice the video into individual clips (or scenes).
  
  -vs  [video, directory]    | standardizes video length, codecs, etc. with ffmpeg bash. needed for concatenation!
  
  -g  [video, directory]     | creates a dynamic, randomized moving video grid with ffmpeg bash commands. this is a legacy file from Court Laureate, not necessary for the project itself :)
```

Due to the sensitive nature of working with video, perfect crop does not currently support multiple commandline options.
Please note that perfectcrop -s needs to be run in the same directory as the source video for shot splicing to occur.

potential errors:
```
  * global loadsave ->   thankfully, this is harmless and most often caused by minute differences in codecs or issues with local reading. I'll hide it.
  * video not found ->   please check permissions, you can do this by running ls -al on the directory & open with chmod commands.
  * file limit hit  ->   grid specific error. please run 'ulimit -n' in terminal to see your current limit, then ulimit -n [whatever] to increase the size to whatever you see fit. please note that this is isolated to your terminal window.
```

Made for Court Laureate, a short film screened at LARPA, December 2023, NY NY.

