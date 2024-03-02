Perfect Crop Tutorial!
---

1. Collect a source video.

   &#9734; for this, we'll be using "yt-dlp" to download a source video of people playing tennis, then use ffmpeg to convert the video to mp4.
    ```
    pip install yt-dlp
    pip install ffmpeg
    yt-dlp "https://www.youtube.com/watch?v=hKgQzRzH3-M" -o tennis_match
    ffmpeg -i tennis_match tennis_match.mp4
    ```
---
2. Ready your directory.
    ```
    mkdir perfectcrop_tutorial
    mv tennis_match.mp4 perfectcrop_tutorial
    ```
---
3. Decide if you'll use the commandline tool, or if you'll run it with python scripts.

   &#9734; this is an important distinction! if you'd prefer to mess around with the code yourself, be sure to run shots.py in the same directory as the source footage, or else the modules won't recognize the videofile.

---
4. Splice up the source file into individual shots using either option.
   ```
   perfectcrop -s tennis_match.mp4
   ```
   ```
   python3 shots.py tennis_match.mp4
   ```
---
5. Move the spliced videos to a set directory, excluding the source clip. I prefer
   
