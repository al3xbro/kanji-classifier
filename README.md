# kanji-classifier
OCR application that classifies almost 3000 Japanese kanji. Full list of characters can be accessed by running ```print_all_characters.py```.

## Dependencies:
* Tensorflow, Keras: 2.12
* NumPy, OpenCV

Note: Follow the guide at https://www.tensorflow.org/guide/gpu to use your GPU for training

## Performance:
* **92%** accuracy for both validation and training sets.
* **0.18** training loss and **0.21** validation loss.

## To Train:
1. Download an image dataset of your choice.
2. Modify the ```config.py``` file to contain the correct paths.
3. Run the ```image_preprocessing.py``` script to process images.
4. Run the ```delete_hiragana.py``` script to remove hiragana from the dataset.
5. Run the ```model_training.py``` script to train your model. Uses data augmentation to help the model generalize.

## Testing:
* Run the ```predicting.py``` script to test your model. 
* Try writing kanji in your own handwriting and testing your model on that. Have fun!

## Resources:
* Datasets ETL8G and ETL9G from [etlcdb](http://etlcdb.db.aist.go.jp/) were used for training and validation.
* Used [etlcdb-image-extractor](https://github.com/choo/etlcdb-image-extractor) to extract images from these datasets. Thank you!
