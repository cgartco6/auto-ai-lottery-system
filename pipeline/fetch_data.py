import pandas as pd

def fetch():

    print("Downloading latest draw data...")

    # placeholder for official lottery data API or scrape
    df = pd.DataFrame()

    df.to_csv("data/raw/draws.csv", index=False)
