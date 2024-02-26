import shutil
import os
import random


imgs_dir = './data_original/images/test'
labels_dir = './data_original/labels/test'

output_dir = './data_100'
for path in [os.path.join(output_dir, 'images', 'test'),
             os.path.join(output_dir, 'labels', 'test')]:
    os.makedirs(path)

max_size = 100

random.seed(0)
selected_paths = random.sample(os.listdir(imgs_dir), k=max_size)

for path in selected_paths:
    img_path = os.path.join(imgs_dir, path)
    label_path = os.path.join(labels_dir, path[:-4] + '.txt')

    shutil.copy(img_path, os.path.join(output_dir, 'images', 'test', path))
    shutil.copy(label_path, os.path.join(output_dir, 'labels', 'test', path[:-4] + '.txt'))
