import os
from PIL import Image, ImageEnhance

# input and output directories
INPUT_DIR = "data/images_original/ETL9G"
OUTPUT_DIR = "data/images_processed"

# makes output directory if doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

# goes through each input label
for label in os.listdir(INPUT_DIR):

    # creates a new output label directory if it doesn't exist
    if (os.path.exists(OUTPUT_DIR + "/" + label)):
        f = open(INPUT_DIR + "/" + label + "/" + ".char.txt", "r")
        print("Processing existing set " + f.read())
        f.close()
    else:
        os.mkdir(OUTPUT_DIR + "/" + label)
        f = open(INPUT_DIR + "/" + label + "/" + ".char.txt", "r")
        print("Processing new set " + f.read())
        f.close()

    # processes each input file
    for file in os.listdir(INPUT_DIR + "/" + label):
        if (file.endswith(".png")):

            im = Image.open(INPUT_DIR + "/" + label + "/" + file)
            newImData = []
            for pixel in im.getdata():
                if pixel < 237:
                    newImData.append(0)
                else:
                    newImData.append(1)

            newIm = Image.new(im.mode, im.size)
            newIm.putdata(newImData)
            newIm = newIm.crop((18, 18, 110, 110))

            # checks for file collisions
            newFileName = file
            # finds new name for collided file
            while (os.path.isfile(OUTPUT_DIR + "/" + label + "/" + newFileName)):
                print("File collision found for " + newFileName)
                newFileName = "{:06d}".format(
                    int(newFileName[0:-4]) + 1) + ".png"
                print("New file name is " + newFileName)

            newIm.save(OUTPUT_DIR + "/" + label + "/" + newFileName)
            im.close()
