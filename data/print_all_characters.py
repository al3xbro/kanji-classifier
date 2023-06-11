import os

from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")
MODEL_PATH = config.get("Paths", "MODEL_PATH")
CLASS_PATH = config.get("Paths", "CLASS_PATH")
PREDICT_PATH = config.get("Paths", "PREDICT_PATH")
TRAINING_IMAGES_PATH = config.get("Paths", "TRAINING_IMAGES_PATH")
UNPROCESSED_IMAGES_PATH = config.get("Paths", "UNPROCESSED_IMAGES_PATH")

for label in sorted(os.listdir(TRAINING_IMAGES_PATH)):
    print (chr(int(label, 16)), end=" ")

print("\nTotal: " + str(len(os.listdir(TRAINING_IMAGES_PATH))) + " characters")
