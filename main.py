# 1. Capture images in intervals (500ms)
# 2. Save the images in catalogue 'img/<date>/`
# 3. Name the images `<gesture>_time.jpg`

import numpy as np
import cv2
import time #Break between the detections
import os
import uuid #naming the image files

def Print(img, *args):
  font                   = cv2.FONT_HERSHEY_SIMPLEX
  bottomLeftCornerOfText = (10,500)
  fontScale              = 1
  fontColor              = (255,255,255)
  thickness              = 1
  lineType               = 2

  cv2.putText(img, str(args), 
      bottomLeftCornerOfText, 
      font, 
      fontScale,
      fontColor,
      thickness,
      lineType)

PATH='img/'
LABELS = ['hello','thanks','yes','no','heart'] # poses
IMAGES_PER_LABEL = 15 # number of images being taken

cap = cv2.VideoCapture(0) # start the webcam
assert cap.isOpened()  # THIS
# Parent Directory path
# mode
mode = 0o666

for label in LABELS:
    # Directory
    directory = label
    # Path
    path_dir = os.path.join(parent_dir, directory)
    os.mkdir(path_dir, mode)
    print("Collecting images for {}".format(label))
    for imgnum in range(IMAGES_PER_LABEL):
        print('Taking img no. ', imgnum, 'for ', label)
        ret, frame = cap.read()
        if not ret:
            print("error while trying to take a photo")
            break  # checking for erros

        name = 'frame' + str(imgnum) + '-' + label
        imgname = os.path.join(Path,label,label+ '.' + '{}.jpg'.format(str(uuid.uuid1()))) #Entire path for the image
        cv2.imwrite(imgname , frame)  # saving the video to the dir
        Print(frame, 'Hello hello')
        cv2.imshow('frame', frame)  # Displaying the video
        time.sleep(0.5)
    time.sleep(0.5)

cap.release()
#################################################################################################



