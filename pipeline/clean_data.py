import pandas as pd

def clean_data():
    print("Cleaning data...")

def clean():

    df = pd.read_csv("data/raw/draws.csv")

    df.dropna(inplace=True)

    df.to_csv("data/processed/clean.csv", index=False)
