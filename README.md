# perfectcrop

Made for Court Laureate, a short film screened at LARPA, December 2023, NY NY.

perfectcrop accepts the following inputs:

  -p   [video, directory]    crop a video or directory of clips to select label (runs perfect_crop.py)

  -s   [video]               create .json file identifying shots (scene changes) in a long form video. shots.py will then splice the video into individual clips                             (or scenes).
  
  -vs  [video, directory]   standardizes video length, codecs, etc. with ffmpeg bash. needed for concatenation!
  
  -ng  [video, directory]   creates a dynamic, randomized moving video grid with ffmpeg bash commands. this is a legacy file from Court Laureate, not necessary                             for the project itself :)


potential errors:
  * global loadsave ->   thankfully, this is harmless and most often caused by minuet differences in codecs or issues with local reading.
  * video not found ->   please check permissions, you can do this by running ls -al on the directory & open with chmod commands.
