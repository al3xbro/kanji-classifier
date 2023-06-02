import os

from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")
MODEL_PATH = config.get("Paths", "MODEL_PATH")
CLASS_PATH = config.get("Paths", "CLASS_PATH")
PREDICT_PATH = config.get("Paths", "PREDICT_PATH")
TRAINING_IMAGES_PATH = config.get("Paths", "TRAINING_IMAGES_PATH")
UNPROCESSED_IMAGES_PATH = config.get("Paths", "UNPROCESSED_IMAGES_PATH")

charList = []
for dataset in os.listdir(UNPROCESSED_IMAGES_PATH):
    for label in os.listdir(os.path.join(UNPROCESSED_IMAGES_PATH, dataset)):
        file = open(os.path.join(UNPROCESSED_IMAGES_PATH, dataset, label, ".char.txt"))
        ch = file.read()
        if ch not in charList:
            charList.append(ch)
        file.close()

print(sorted(charList))
print("Total: " + str(len(charList)) + " characters")
