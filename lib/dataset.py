import os
import numpy as np
import torch
from torch.utils.data import Dataset
from sklearn.model_selection import train_test_split

from lib.utils import *

class NailDataset(Dataset):
    def __init__(self, origin_path, label_path):
        self.origin_path = origin_path
        self.label_path = label_path

        origin_name, origin_npy = self._list_name(origin_path)
        label_name, label_npy = self._list_name(label_path)

        same = self._check_same(origin_name, label_name)
        if not same:
            raise RuntimeError('Check the origin and label image.')

        self.origin = self._build_matrix(origin_npy, 3, 480)
        self.label = self._build_matrix(label_npy, 1, 464)

    def __getitem__(self, index):
        data = self.origin[index]
        label = self.label[index]

        return data, label

    def __len__(self):
        return self.origin.size(0)

    def _build_matrix(self, npy, ch, shape):
        data = torch.empty(len(npy), ch, shape, shape)
        for i in range(len(npy)):
            tensor = self._npy_to_tensor(np.load(npy[i]), ch, shape)
            data[i] = tensor

        return data

    def _npy_to_tensor(self, npy, ch, shape):
        tensor = torch.empty(ch, shape, shape)
        if ch > 1:
            for i in range(ch):
                tensor[i, :, :] = torch.tensor(npy[:, :, i])

        elif ch == 1:
            tensor = torch.tensor(npy).float()
        else:
            raise RuntimeError('Invalid channel number')

        return tensor

    def _check_same(self, origin, label):
        check = True
        for i in range(len(origin)):
            if origin[i] != label[i]:
                check = False

        return check

    def _list_name(self, path):
        npy = []
        name = []
        for file in os.listdir(path):
            if file.endswith('.npy'):
                name.append(file.replace('.npy', ''))
                npy.append(path + '/' + file)

        return name, npy


