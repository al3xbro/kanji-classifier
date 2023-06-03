# ann-ocr-kanji
OCR application that classifies 3000+ Japanese kanji, hiragana, and katakana. Full list of characters can be accessed by running ```print_all_characters.py```. Webapp still in the works.

## Dependencies:
* Tensorflow, Keras: 2.12
* NumPy, OpenCV

Note: Follow the guide at https://www.tensorflow.org/guide/gpu to use your GPU for training

## Performance:
* **94%** accuracy for both validation and training sets.
* **0.23** training loss and **0.26** validation loss.

## To Train:
1. Download an image dataset of your choice.
2. Modify the ```config.py``` file to contain the correct paths.
3. Run the ```image_preprocessing.py``` script to process images.
4. Run the ```model_training.py``` script to train your model.

## Testing:
* Run the ```predicting.py``` script to test your model. 
* Try writing kanji in your own handwriting and testing your model on that. Have fun!

## Resources:
* Datasets ETL5, ETL8G, and ETL9G from http://etlcdb.db.aist.go.jp/ were used for training and validation.
* Used https://github.com/choo/etlcdb-image-extractor to extract images from the datasets. Thank you!
