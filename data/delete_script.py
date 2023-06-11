import os 
import shutil

for image in os.listdir("data/images_processed"):
    if int(image, 16) >= 12353 and int(image, 16) <= 12436:
        print("removing " + image + " " + chr(int(image, 16)))
        shutil.rmtree("data/images_processed/" + image)