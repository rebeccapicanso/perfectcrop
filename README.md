# Perfect Crop

Perfect Crop is now released as a commandline tool!
```
pip install perfectcrop
```
v1 notes:
- Please note that at this moment, only -g --grid will accept directory input. Will be patched in the coming days!
- There's not yet an array storing acceptable labels. Please visit the COCO website for usable options. In v2, I'll be adding a webscraping element to append acceptable labels, in addition to other annotation support.
- By default, atm perfectcrop works best with detecting a relatively static object. there's ways to track movement & crop with this algorithm, but I haven't yet figured out how to render out finishing quality video. stay tuned!

---

Perfect Crop will locate a detected object within a video clip, find its average location, and create a cropped clip from the center. Object detection models splice videos into individual frames & then run detection on static images - Perfect Crop transmutes this into workable video.

This tool is most useful when used on large clip sets (200+). It was built for the quick processing of over 50 hours of live-stream footage!

As a test example, searching the video for "cell phone":
Source Clip            |  Detected Object
:-------------------------:|:-------------------------:
![](https://github.com/rebeccapicanso/perfect_crop/blob/main/readme_source.gif)| ![](https://github.com/rebeccapicanso/perfect_crop/blob/main/readme_detected.gif)

Perfect Crop's algorithm was built around Hugging Face's [hustvl/yolo](https://www.google.com/search?q=hustvl%2Fyolo-tiny&rlz=1C5CHFA_enUS997US998&oq=yolostiny+hu&gs_lcrp=EgZjaHJvbWUqCggBEAAYChgWGB4yBggAEEUYOTIKCAEQABgKGBYYHjINCAIQABiGAxiABBiKBdIBCDMwNTRqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8) sets, a series of vision transformer models trained on the [COCO](https://cocodataset.org/#home) dataset. It's computationally light on any system. At the moment, the algorithm is set only for models using YOLO bounding box annotations - so if you want to swap out the model, keep that in mind.

Calculating the center pixel of a bounding box requires backward engineering of detection algorithms - I'm excited to release support for other annotations in v2.

---
Perfect Crop can also label scenes with content and object locations, as well as index a video & splice it into individual scenes without quality loss.

```
perfectcrop accepts the following inputs:

  -i   [input]                              | input, single file path or directory (for grid)

and one of the following..

  -p, --perfect_crop  [video or directory]  | crop a video or directory of clips to select label (runs perfect_crop.py)

  -s, --shots   [video]                     | create .json file identifying shots (scene changes) in a long form video. shots.py will then splice the video into individual clips (or scenes).
  
  -t, --standardize [video or directory]    | standardizes video length, codecs, etc. with ffmpeg bash. needed for concatenation!
  
  -g, --grid   [video or directory]         | creates a dynamic, randomized moving video grid with ffmpeg bash commands. this is a legacy file from Court Laureate, not necessary for the project itself :)

followed by output directory, if left blank resorts to current directory..

  -o  [output]                              | output directory, will create for you
```
example usage:
```
perfectcrop -i tennis_match.mp4 -p -o tennis
```
Function arguements (-p, -s, -t, -g) are not positionally bound.. but I'd keep them in the middle anyways.

Perfect Crop does not yet support multiple function options.
Please note that perfectcrop -s needs to be run in the same directory as the source video for shot splicing to occur.

---


potential errors:
```
  * global loadsave ->   thankfully, this is harmless and most often caused by minute differences in codecs or issues with local reading. I'll hide it.
  * video not found ->   please check permissions, you can do this by running ls -al on the directory & open with chmod commands.
  * file limit hit  ->   grid specific error. please run 'ulimit -n' in terminal to see your current limit, then ulimit -n [whatever] to increase the size to whatever you see fit. please note that this is isolated to your terminal window.
```

---
**Made for Court Laureate, a short film screened at LARPA, December 2023, NY NY.
Although one cannot patent an algorithm, please respect the open-source nature of this project & all derivatives.**

