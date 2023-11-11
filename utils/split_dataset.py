#!/usr/bin/env python3

import os
import tensorflow as tf
import shutil
import sys


def load_data(src):
    """
        load data from combined images-labels datasets 
    """

    image_files = sorted([
        filename for filename in os.listdir(src)
        if filename.endswith('.jpg')
    ])

    label_files = sorted([
        filename for filename in os.listdir(src)
        if filename.endswith('.txt')
    ])
    
    data = tf.data.Dataset.from_tensor_slices((image_files, label_files))

    return data

def create_folder(dest, split_type):
    """
        creating destination folder structure
    """

    contained_data = ['images', 'labels']

    for split in split_type:
        os.makedirs(os.path.join(dest, split))
        for data_type in contained_data:
            os.makedirs(os.path.join(dest, split, data_type))


def split_data(data, src, dest, split_type):
    """
        splitting data and save it to destination path
    """

    TRAIN_SPLIT = 0.8
    TEST_VAL_SPLIT = 0.5
    BUFFER_SIZE = int(len(data))

    data = data.shuffle(BUFFER_SIZE, reshuffle_each_iteration=False)
    train_ds = data.take(int(TRAIN_SPLIT * len(data)))
    temp = data.skip(int(TRAIN_SPLIT * len(data)))
    val_ds = temp.take(int(TEST_VAL_SPLIT * len(temp)))
    test_ds = temp.skip(int(TEST_VAL_SPLIT * len(temp)))

    del temp

    splitted_data = [train_ds, val_ds, test_ds]

    for idx, tf_data in enumerate(splitted_data):
        for paired_data in tf_data.as_numpy_iterator():
            image, label = paired_data
            target_img_path = os.path.join(dest, split_type[idx], 'images', image.decode('utf-8'))
            label_img_path = os.path.join(dest, split_type[idx], 'labels', label.decode('utf-8'))
            shutil.copy(os.path.join(src, image.decode('utf-8')), target_img_path)
            shutil.copy(os.path.join(src, label.decode('utf-8')), label_img_path)
        print(f'\t{split_type[idx]} created!')

if __name__ == '__main__':
    """
        usage : python3 split_dataset.py [BASE_PATH] [DEST_PATH]
    """

    BASE_PATH = sys.argv[1]
    DEST_PATH = os.path.join(sys.argv[2], 'datasets')

    split_type = ['train', 'val', 'test']

    data = load_data(BASE_PATH)

    create_folder(DEST_PATH, split_type)

    split_data(data, BASE_PATH, DEST_PATH, split_type)
