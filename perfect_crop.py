from moviepy.editor import VideoFileClip
from PIL import Image
from transformers import pipeline
import itertools
import cv2

# please pre-bulk cut videos, example set for 2 seconds from start
# for file in *.mp4; do ffmpeg -ss 00:00:00.00 -i in.mp4 -t 2 -map 0 test_dump/${file} ; done

# searches through a video and extracts images of particular objects

# please make sure you're using a term recognized by the model
print("Perfect crop currently runs on HuggingFace's models with YOLO annotation, other annotations are to be completed later!")
LABEL = input("Please enter the label you are looking for, either person or cellphone:")

# run the code only ever X frames (5 by default)
SKIP = 5

# build out pipeline
pipe = pipeline("object-detection", model="hustvl/yolos-tiny")

# !!!!! Default model info !!!!!
# https://cocodataset.org/#explore

# please pre-bulk cut videos, example set for 2 seconds from start
# for file in *.mp4; do ffmpeg -ss 00:00:00.00 -i in.mp4 -t 2 -map 0 test_dump/${file} ; done

# you could bulk remove in code or just sort finder by date modified

average_center = []

def save_images(videofile, search=LABEL):
    clip = VideoFileClip(videofile)
    index = 0
    frame_no = 0

    for frame in clip.iter_frames():
        frame_no += 1
        if frame_no % SKIP != 0:
            continue

        # print("Detecting objects in frame", frame_no)

        image = Image.fromarray(frame)

        results = pipe(image)

        for r in results:
            # print(r)
            if r["label"] == search:
                box = r["box"]

                xmin = box["xmin"]
                ymin = box["ymin"]
                xmax = box["xmax"]
                ymax = box["ymax"]

                print(xmin,ymin,xmax,ymax)

                # must make sure that the box is not out of bounds
                if xmin > 0 and xmax > 0 and ymin > 0 and ymax > 0:
                    # this is giving a harmless global error... not sure why
                    img_read= cv2.imread(r'image.png')
                    
                    cv2.rectangle(img_read,(xmin,ymin),(xmax,ymax),(0,0,255),3)
                    center_x = int((xmin+xmax)//2)
                    center_y = int((ymin+ymax)//2)

                    center = [center_x,center_y]
                    average_center.append(center)
                    print(center)

                    index += 1
                else:
                    print("out of bounds")
                    continue

def average_crop(videofile, average_center):
    print(average_center)

    true_center= [sum(x)/len(x) for x in zip(*average_center)]

    # now we have the coordinates of the box, we can crop the video
    clip = VideoFileClip(videofile)

    midpoint_x = true_center[0]
    midpoint_y = true_center[1]

    # jam in whatever coordinates you want, size in pixels
    width = 300
    height = 300

    video = clip.crop(x_center=midpoint_x, y_center=midpoint_y, width=width, height=height)

    # write it as the same name as the video file + _cropped
    video.write_videofile(f'{videofile}_person.mp4')





    
if __name__ == "__main__":
    import sys

    for f in sys.argv[1:]:
        save_images(f, LABEL)
    
        average_crop(f, average_center)
