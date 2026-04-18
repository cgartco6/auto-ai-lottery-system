import pandas as pd

def number_frequency(df):

    numbers = pd.concat([
        df["n1"], df["n2"], df["n3"],
        df["n4"], df["n5"]
    ])

    freq = numbers.value_counts().sort_values(ascending=False)

    return freq
