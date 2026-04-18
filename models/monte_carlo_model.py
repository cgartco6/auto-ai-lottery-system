import numpy as np

def monte_carlo(prob, runs=100000):

    results = []

    for _ in range(runs):

        results.append(sorted(np.random.choice(range(1,51),5,replace=False)))

    return results
