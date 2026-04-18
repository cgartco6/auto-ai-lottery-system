import pandas as pd

def build_features():

    df = pd.read_csv("data/processed/clean.csv")

    df["sum"] = df.sum(axis=1)

    df.to_csv("data/processed/features.csv", index=False)
