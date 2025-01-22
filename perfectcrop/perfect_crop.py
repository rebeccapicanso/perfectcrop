from moviepy.editor import VideoFileClip
from PIL import Image
from transformers import pipeline
import cv2
import os
import logging

logging.basicConfig(level=logging.ERROR)
cv2.setLogLevel(cv2.LOG_LEVEL_ERROR)

# please make sure you're using a term recognized by the model
print("Perfect crop currently runs on HuggingFace's models with YOLO annotation, support other annotations are to be completed later.\n")

print("please make sure you're using a term recognized by the model")
print("https://cocodataset.org/#explore")

LABEL = input("Please enter the label you are looking for.\n"
             + "Labels must be searchable at https://cocodataset.org/#explore:" )

# run the code only ever X frames (5 by default)
SKIP = 5

# build out pipeline
pipe = pipeline("object-detection", model="hustvl/yolos-tiny")

average_center = []

def save_images(input, output, search=LABEL):

    # set input as videofile
    videofile = input
    clip = VideoFileClip(videofile)
    
    # initializing..
    index = 0
    frame_no = 0

    # make output directory
    if not os.path.exists("output"):
        os.makedirs("output")

    
    for frame in clip.iter_frames():
        frame_no += 1
        if frame_no % SKIP != 0:
            continue

        # print("Detecting objects in frame", frame_no)
        
        # calling Pillow's Image function
        image = Image.fromarray(frame)

        # then tossing that image into the pipeline
        # i.e. is it there or not?
        results = pipe(image)

        for r in results:
            # print(r)
            
            # if the labeled object is in frame, yay
            # YOLO annotative obj. detect algos draw the bounding box (the square it throws around something)
            # based on max & min values. here, i'm just looking at the cross points.
            # a bounding box is an ephemeral thing. it's not recorded, its an internal throw away process.
            
            if r["label"] == search:
                box = r["box"]

                xmin = box["xmin"]
                ymin = box["ymin"]
                xmax = box["xmax"]
                ymax = box["ymax"]

                if xmin > 0 and xmax > 0 and ymin > 0 and ymax > 0:

                    img_read = cv2.imread(r'image.png')
                    cv2.rectangle(img_read,(xmin,ymin),(xmax,ymax),(0,0,255),3)

                    center_x = int((xmin+xmax)//2)
                    center_y = int((ymin+ymax)//2)
                    center = [center_x,center_y]
                    average_center.append(center)
                    index += 1

                else:
                    print("out of bounds")
                    continue

    def average_crop():

        print(average_center)
        true_center= [sum(x)/len(x) for x in zip(*average_center)]

        clip = VideoFileClip(videofile)

        midpoint_x = true_center[0]
        midpoint_y = true_center[1]
        width = 300
        height = 300

        video = clip.crop(x_center=midpoint_x, y_center=midpoint_y, width=width, height=height)
        video.write_videofile(f'{input}_label.mp4')
    
    average_crop()
    
    if not os.path.exists(f'{output}'):
        os.makedirs(f'{output}')
    
    os.system(f'mv *.mp4 {output}')
    os.system(f'mv {output}/{input} .')

    # notify file location
    print("Files are in " + output)

if __name__ == "__main__":
    # output is init by cli.py
    # default
    output = "output.mp4"
    save_images(input, output)
