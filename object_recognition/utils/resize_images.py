#!/usr/bin/env python3

import tensorflow as tf
import os
import sys


def resize_images(source, destination, target_size=(512, 512)):
    """
        resize images to target size within specific folder
    """

    classes = os.listdir(source)
    for label in classes:
        folder_path = os.path.join(f'./raw/{label}')
        os.mkdir(os.path.join(destination, label))
        for idx, filename in enumerate(os.listdir(folder_path)):
            filepath = os.path.join(folder_path, filename)
            img = tf.keras.utils.load_img(filepath, target_size=target_size)
            img.save(os.path.join(destination, label, f'{label}_{idx}.jpg'))
        print(f'Resize {label} Folder Completed!')


if __name__ == '__main__':
    SRC_DIR = sys.argv[1]
    DEST_DIR = sys.argv[2]
    resize_images(SRC_DIR, DEST_DIR)
