import os
dataset_path = 'D:/Anaconda/Driver monitoring system/dataset/test/'
path = os.path.join(dataset_path, 'smoking')

files = os.listdir(path)

for file in files:
    if file.endswith('.jpeg'):
        print(file)