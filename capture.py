

import numpy as np
import cv2
import time #Break between the detections
import os
import uuid #naming the image files

Path='C:\\Users\\Seana\\RealTimeObjectDetection\\Tensorflow\\workspace\\images\\Collected_images'

#Defining the images count and type
labels = ['hello','thanks','yes','no','heart'] #poses
number_imgs = 15 #number of images being taken

cap = cv2.VideoCapture(0) #start the webcam
assert cap.isOpened()  # THIS
# Parent Directory path
parent_dir = "C:\\Users\\Seana\\RealTimeObjectDetection\\Tensorflow\\workspace\\images\\Collected_images"
# mode
mode = 0o666

for label in labels:
    # Directory
    directory = label
    # Path
    path_dir = os.path.join(parent_dir, directory)
    os.mkdir(path_dir, mode)
    print("Collecting images for {}".format(label))
    for imgnum in range(number_imgs):
        print('Taking img no. ', imgnum, 'for ', label)
        ret, frame = cap.read()
        if not ret:
            print("error while trying to take a photo")
            break  # checking for erros

        name = 'frame' + str(imgnum) + '-' + label
        imgname = os.path.join(Path,label,label+ '.' + '{}.jpg'.format(str(uuid.uuid1()))) #Entire path for the image
        cv2.imwrite(imgname , frame)  # saving the video to the dir
        cv2.imshow('frame', frame)  # Displaying the video
        time.sleep(0.5)
      #  if cv2.waitKey(1) & 0xFF == ord('q'):
      #      break
    time.sleep(0.5)

cap.release()
#################################################################################################



