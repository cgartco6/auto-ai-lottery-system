import pandas as pd
import itertools
from collections import Counter


DATA_FILE = "data/raw/powerball_history.csv"


def generate():

    df = pd.read_csv(DATA_FILE)

    numbers = pd.concat([
        df["n1"],
        df["n2"],
        df["n3"],
        df["n4"],
        df["n5"]
    ])

    freq = numbers.value_counts()

    most_common = list(freq.index[:20])

    combos = list(itertools.combinations(most_common, 5))

    scores = []

    for combo in combos:

        score = sum(freq[n] for n in combo)

        scores.append((combo, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    top13 = scores[:13]
    top6 = scores[:6]

    return top13, top6
