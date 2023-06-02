import os
import cv2
import numpy as np
import tensorflow as tf

from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")
MODEL_PATH = config.get("Paths", "MODEL_PATH")
CLASS_PATH = config.get("Paths", "CLASS_PATH")
PREDICT_PATH = config.get("Paths", "PREDICT_PATH")
TRAINING_IMAGES_PATH = config.get("Paths", "TRAINING_IMAGES_PATH")
UNPROCESSED_IMAGES_PATH = config.get("Paths", "UNPROCESSED_IMAGES_PATH")

# makes output directory if doesn't exist
if not os.path.exists(TRAINING_IMAGES_PATH):
    os.mkdir(TRAINING_IMAGES_PATH)

# goes through each input label
for dataset in os.listdir(UNPROCESSED_IMAGES_PATH):
    for label in os.listdir(os.path.join(UNPROCESSED_IMAGES_PATH, dataset)):
        # creates a new output label directory if it doesn't exist
        if os.path.exists(os.path.join(TRAINING_IMAGES_PATH, dataset, label)):
            f = open(os.path.join(UNPROCESSED_IMAGES_PATH, label, ".char.txt"), "r")
            print("Processing existing set " + f.read())
            f.close()
        else:
            os.mkdir(os.path.join(TRAINING_IMAGES_PATH, dataset, label))
            f = open(os.path.join(UNPROCESSED_IMAGES_PATH, label, ".char.txt"), "r")
            print("Processing new set " + f.read())
            f.close()

        # processes each input file
        for file in os.listdir(os.path.join(UNPROCESSED_IMAGES_PATH, dataset, label)):
            if (file.endswith(".png")):

                im = cv2.imread(os.path.join(UNPROCESSED_IMAGES_PATH, dataset, label, file))
                im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

                # if downscaling
                if im.shape[0] >= 110 and im.shape[1] >= 110:
                    im = im[18:110, 18:110]
                # if upscaling
                else:
                    im = np.atleast_3d(im)
                    im = tf.image.resize(im, (97, 97), preserve_aspect_ratio=True)
                    im = np.squeeze(im)
                    im = im.copy()

                for y in range(0, 92):
                    for x in range(0, 92):
                        if im[y][x] < 237:
                            im[y][x] = 1
                        else:
                            im[y][x] = 0

                # checks for file collisions
                newFileName = file
                # finds new name for collided file
                while (os.path.isfile(os.path.join(TRAINING_IMAGES_PATH, label, newFileName))):
                    print("File collision found for " + newFileName)
                    newFileName = "{:06d}".format(
                        int(newFileName[0:-4]) + 1) + ".png"
                    print("New file name is " + newFileName)

                cv2.imwrite(os.path.join(TRAINING_IMAGES_PATH, label, newFileName), im)
