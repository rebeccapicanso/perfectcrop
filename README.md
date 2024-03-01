# Perfect Crop

Perfect Crop will locate a detected object within a video clip, find its average location, and create a cropped clip from the center. Object detection models splice videos into individual frames & then run detection on static images - Perfect Crop transmutes this into workable video.

This tool is most useful when used on large clip sets (200+). It was built for the quick processing of over 50 hours of live-stream footage!

As a test example, searching the video for "cell phone":
Source Clip            |  Detected Object
:-------------------------:|:-------------------------:
![](https://github.com/rebeccapicanso/perfect_crop/blob/main/readme_source.gif)| ![](https://github.com/rebeccapicanso/perfect_crop/blob/main/readme_detected.gif)

Perfect Crop's algorithm was built around Hugging Face's [hustvl/yolo](https://www.google.com/search?q=hustvl%2Fyolo-tiny&rlz=1C5CHFA_enUS997US998&oq=yolostiny+hu&gs_lcrp=EgZjaHJvbWUqCggBEAAYChgWGB4yBggAEEUYOTIKCAEQABgKGBYYHjINCAIQABiGAxiABBiKBdIBCDMwNTRqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8) sets, a series of vision transformer models trained on the [COCO](https://cocodataset.org/#home) dataset. It's computationally light on any system. At the moment, the algorithm is set only for models using YOLO bounding box annotations - so if you want to swap out the model, keep that in mind.

Calculating the center pixel of a bounding box is a new idea & requires backward engineering of detection algorithms - I'm excited to release support for other annotations in v2.

---
Perfect Crop can also label scenes with content and object locations, as well as index a video & splice it into individual scenes without quality loss.

```
perfectcrop accepts the following inputs:

  -p   [video or directory]    | crop a video or directory of clips to select label (runs perfect_crop.py)

  -s   [video]                 | create .json file identifying shots (scene changes) in a long form video. shots.py will then splice the video into individual clips (or scenes).
  
  -vs  [video or directory]    | standardizes video length, codecs, etc. with ffmpeg bash. needed for concatenation!
  
  -g   [video or directory]    | creates a dynamic, randomized moving video grid with ffmpeg bash commands. this is a legacy file from Court Laureate, not necessary for the project itself :)

  -l   [video or directory]    | for a select object, identifies what shots that label appears, and then records the average location of that object.
```

Due to the sensitive nature of working with video, Perfect Crop does not currently support multiple command line options.
Please note that perfectcrop -s needs to be run in the same directory as the source video for shot splicing to occur.

potential errors:
```
  * global loadsave ->   thankfully, this is harmless and most often caused by minute differences in codecs or issues with local reading. I'll hide it.
  * video not found ->   please check permissions, you can do this by running ls -al on the directory & open with chmod commands.
  * file limit hit  ->   grid specific error. please run 'ulimit -n' in terminal to see your current limit, then ulimit -n [whatever] to increase the size to whatever you see fit. please note that this is isolated to your terminal window.
```

---
**Made for Court Laureate, a short film screened at LARPA, December 2023, NY NY.
Although one cannot patent an algorithm, please respect the open-source nature of this project & all derivatives.**

