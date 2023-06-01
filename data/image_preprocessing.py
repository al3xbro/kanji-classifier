import os
import cv2

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
for label in os.listdir(UNPROCESSED_IMAGES_PATH):

    # creates a new output label directory if it doesn't exist
    if (os.path.exists(os.path.join(TRAINING_IMAGES_PATH, label))):
        f = open(os.path.join(UNPROCESSED_IMAGES_PATH, label, ".char.txt"), "r")
        print("Processing existing set " + f.read())
        f.close()
    else:
        os.mkdir(os.path.join(TRAINING_IMAGES_PATH, label))
        f = open(os.path.join(UNPROCESSED_IMAGES_PATH, label, ".char.txt"), "r")
        print("Processing new set " + f.read())
        f.close()

    # processes each input file
    for file in os.listdir(os.path.join(UNPROCESSED_IMAGES_PATH, label)):
        if (file.endswith(".png")):

            im = cv2.imread(os.path.join(UNPROCESSED_IMAGES_PATH, label, file))
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            im = im[18:110, 18:110]

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
