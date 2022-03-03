from itertools import count
import os
import cv2
import random


def file_split(src_dir, train_dir, val_dir, img_names):
    count = 0
    for name in img_names:
        img_path = os.path.join(src_dir, name)
        img = cv2.imread(img_path)
        if count < 574:
            cv2.imwrite(os.path.join(train_dir, name), img)
            count += 1
        elif count >= 574 and count < 689:
            cv2.imwrite(os.path.join(val_dir, name), img)
            count += 1
        else:
            break



if __name__=="__main__":
    src_dir='D:/Anaconda/Driver monitoring system/dataset/renamed_temp/yawn'

    train_dir = 'D:/Anaconda/Driver monitoring system/dataset/balanced dataset/working_training_data/yawn/'
    val_dir = 'D:/Anaconda/Driver monitoring system/dataset/balanced dataset/working_validation_data/yawn/'

    img_names = os.listdir(src_dir)

    random.shuffle(img_names)

    file_split(src_dir, train_dir, val_dir, img_names)