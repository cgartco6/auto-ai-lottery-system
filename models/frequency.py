import numpy as np

def frequency_model(data):

    return np.bincount(data.flatten(), minlength=51)
