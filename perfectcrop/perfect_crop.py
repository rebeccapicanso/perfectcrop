from moviepy.editor import VideoFileClip
from PIL import Image
from transformers import pipeline
import itertools
import cv2

# please make sure you're using a term recognized by the model
print("Perfect crop currently runs on HuggingFace's models with YOLO annotation, support other annotations are to be completed later.")

# this ia rudimentary for testing purposes
# please make sure you're using a term recognized by the model
#
# https://cocodataset.org/#explore

LABEL = input("Please enter the label you are looking for.\n"
             + "Labels must be searchable at https://cocodataset.org/#explore:" )

# run the code only ever X frames (5 by default)
SKIP = 5

# build out pipeline
pipe = pipeline("object-detection", model="hustvl/yolos-tiny")



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

