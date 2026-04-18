import numpy as np

def ensemble(models):

    return np.mean(models, axis=0)
