import os
import numpy as np

import tensorflow as tf
assert tf.__version__.startswith('2')

from tflite_model_maker import model_spec, image_classifier
from tflite_model_maker.config import ExportFormat, QuantizationConfig
from tflite_model_maker.image_classifier import DataLoader

import matplotlib.pyplot as plt

dataset_path = 'D:\Anaconda\Driver monitoring system\dataset'
evaluate_data = DataLoader.from_folder(os.path.join(dataset_path, 'test'))
train_data = DataLoader.from_folder(os.path.join(dataset_path, 'test'))
test_data, val_data = evaluate_data.split(0.5)

#print(len(train_data), len(test_data), len(val_data))
spec = 'efficientnet_lite0'
#spec = model_spec.get('mobilenet_v2')
#spec = model_spec.get('resnet_50')

img_classifier = image_classifier.create(train_data=train_data, validation_data=val_data, model_spec=spec, epochs=10, batch_size=16,\
    dropout_rate=0.45, use_hub_library=False, model_dir='./checkpoints', train_whole_model=True)

loss, accuracy = img_classifier.evaluate(test_data)
print(loss, accuracy)
#img_classifier.export('model_10_16_lite0_v2')