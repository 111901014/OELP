# DATA
This folder contains dataset of lung ultrasound images and videos.

## CONVEX AND LINEAR
Each folder contains data related to convex and linear probe seperately and we can use either or both for building the dataset.

## PROCESSING VIDEOS
The CODES/data_generation.py module processes the videos and returns the frames as images. Both the processed images from the videos and the existing images are saved to a new folder 'DATA/IMAGE_DATASET' which can be used for training and testing the models.