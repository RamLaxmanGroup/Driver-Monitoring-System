import os
from random import shuffle
import numpy as np

import tensorflow as tf
assert tf.__version__.startswith('2')

from tflite_model_maker import model_spec, image_classifier
from tflite_model_maker.config import ExportFormat, QuantizationConfig
from tflite_model_maker.image_classifier import DataLoader

import matplotlib.pyplot as plt

dataset_path = './dataset/balanced dataset'
""" print(os.path.join(dataset_path, 'working_validation_data')) """
evaluate_data = DataLoader.from_folder(os.path.join(dataset_path, 'working_validation_data'))
train_data = DataLoader.from_folder(os.path.join(dataset_path, 'working_training_data'))
val_data, test_data = evaluate_data.split(0.90)

print(len(train_data), len(val_data), len(test_data))
spec = 'efficientnet_lite0'
#spec = model_spec.get('mobilenet_v2')
#spec = model_spec.get('resnet_50')

img_classifier = image_classifier.create(train_data=train_data, validation_data=val_data, model_spec=spec, epochs=1000, batch_size=8,\
    dropout_rate=0.45, use_hub_library=False, model_dir='./checkpoints', train_whole_model=True, shuffle=False, use_augmentation=True)

loss, accuracy = img_classifier.evaluate(test_data)
print(loss, accuracy)
img_classifier.export('./models/bus_best_8_lite0_5classes')