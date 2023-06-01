import os
from PIL import Image
from config import MODEL_PATH, CLASS_PATH, PREDICT_PATH, TRAINING_IMAGES_PATH, UNPROCESSED_IMAGES_PATH

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

            im = Image.open(os.path.join(UNPROCESSED_IMAGES_PATH, label, file))
            newImData = []
            for pixel in im.getdata():
                if pixel < 237:
                    newImData.append(1)
                else:
                    newImData.append(0)

            newIm = Image.new(im.mode, im.size)
            newIm.putdata(newImData)
            newIm = newIm.crop((18, 18, 110, 110))

            # checks for file collisions
            newFileName = file
            # finds new name for collided file
            while (os.path.isfile(os.path.join(TRAINING_IMAGES_PATH, label, newFileName))):
                print("File collision found for " + newFileName)
                newFileName = "{:06d}".format(
                    int(newFileName[0:-4]) + 1) + ".png"
                print("New file name is " + newFileName)

            newIm.save(os.path.join(TRAINING_IMAGES_PATH, label, newFileName))
            im.close()
