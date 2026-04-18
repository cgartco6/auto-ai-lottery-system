import numpy as np

def bayes(prior, likelihood):
    return (prior * likelihood) / (prior.sum() + 1e-9)
