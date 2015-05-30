import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('seeds_dataset.txt',delim_whitespace=True,
                   names =['area',
                   'perimeter',
                   'compactness',
                   'length of kernel',
                   'width of kernel',
                   'asymmetry coefficien',
                   'length of kernel groove',
                   'local'])
