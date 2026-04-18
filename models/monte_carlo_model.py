import numpy as np

def monte_carlo_predictions(freq, simulations=200000):

    numbers = freq.index.values
    weights = freq.values / freq.values.sum()

    combos = []

    for _ in range(simulations):

        draw = np.random.choice(
            numbers,
            size=5,
            replace=False,
            p=weights
        )

        combos.append(tuple(sorted(draw)))

    return combos
