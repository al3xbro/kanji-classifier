# prints every kanji in the dataset

import os

INPUT_PATH = "data/images_original/ETL9G"

class_list = []
for folder in os.listdir(INPUT_PATH):
    file = open(os.path.join(
        "data/images_original/ETL9G", folder, ".char.txt"), "r")
    class_list.append(file.read())
    file.close()

print(class_list)
