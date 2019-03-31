import os
import numpy as np
from skimage import io, transform

def GrabMiddle(image):
    image = image[:, 80: 560, :]
    return image

def LabelImage(image):
    r = np.array(image[:, :, 0], dtype = np.float)
    g = np.array(image[:, :, 1], dtype = np.float)
    b = np.array(image[:, :, 2], dtype = np.float)

    out = 2 * g - r - b
    label = np.where(out > 1, 1, 0)

    return label

def FolderLabel(file_path, save_path):
    image_path = []
    image_name = []
    for file in os.listdir(file_path):
        if file.endswith('.jpg'):
            image_name.append(file)
            image_path.append(file_path + '/' + file)

    for i in range(len(image_path)):
        image = io.imread(image_path[i])
        image = GrabMiddle(image)
        image = transform.resize(image, (464, 464))
        label = LabelImage(image)
        label = label.reshape(1, 464, 464)

        np.save(save_path + '/' + image_name[i].replace('.jpg', '.npy'), label)

def FolderImage(file_path, save_path):
    image_path = []
    image_name = []
    for file in os.listdir(file_path):
        if file.endswith('.jpg'):
            image_name.append(file)
            image_path.append(file_path + '/' + file)

    for i in range(len(image_path)):
        image = io.imread(image_path[i])
        image = GrabMiddle(image)
        image = image / np.max(image)

        np.save(save_path + '/' + image_name[i].replace('.jpg', '.npy'), image)


