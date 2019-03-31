import sys
import numpy as np

from lib.utils import *
from lib.dataprocessing import *

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 preprocessing.py [origin image path] [origin npy save path] [label image path] [label image save path]]')
        exit(0)

    FolderImage(sys.argv[1], sys.argv[2])
    FolderLabel(sys.argv[3], sys.argv[4])


