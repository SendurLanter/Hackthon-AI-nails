import os
import sys
import time
import numpy as np
import torch
import torchvision
import torchvision.transforms as transforms
import torch.cuda as cuda
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import Adam
from torch.utils.data import DataLoader

from lib.utils import *
from lib.model import UNet
from lib.dataset import NailDataset

def TrainModel(model, saving_name, epochs, batch_size, device, save = True):
    if device < 0:
        env = torch.device('cpu')
        print('Envirnment setting done, using device: cpu')
    else:
        torch.backends.cudnn.benchmark = True
        cuda.set_device(device)
        env = torch.device('cuda:' + str(device))
        print('Envirnment setting done, using device: CUDA_' + str(device))

    model.float().to(env)
    criterion = nn.BCELoss()
    criterion.to(env)
    optim = Adam(model.parameters())

    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    train_set = NailDataset('./origin_npy', './label_npy')

    train_loader = DataLoader(train_set, batch_size = batch_size, shuffle = True)

    print('Model Structure:')
    print(model)

    for epoch in range(epochs):
        print('Start training epoch:', epoch + 1)
        train_loss = []
        for iter, data in enumerate(train_loader):
            train_x, train_y = data
            train_x = train_x.float().to(env)
            train_y = train_y.float().to(env)

            optim.zero_grad()

            out = model(train_x)

            loss = criterion(out, train_y)
            train_loss.append(loss)
            loss.backward()

            optim.step()

            if iter != 0 and iter % 10 == 0:
                print('Iter: ', iter, ' | Loss: %6f' % loss.detach())

        train_loss = torch.tensor(train_loss)
        print('Epoch:', epoch + 1, '| Loss:', torch.mean(train_loss))

    if save:
        torch.save(model, saving_name + '.pkl')

    print('All training process done.')

def LoadModel(name):
    model = None
    for file in os.listdir('./'):
        if file == name + '.pkl':
            model = torch.load(name + '.pkl')
            print('Load model', name, 'success.')
            break

    if model == None:
        return UNet()
    else:
        return model

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python3 train.py [model name] [epoch] [batch_size] [device]')
        exit(0)

    start_time = time.time()
    model = LoadModel(sys.argv[1])
    TrainModel(model, sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    print('All process done, cause %s seconds.' % (time.time() - start_time))


