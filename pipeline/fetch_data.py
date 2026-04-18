import pandas as pd
import requests

DATA_URL = "https://raw.githubusercontent.com/lottery-results/powerball-data/main/sa_powerball.csv"

def fetch_lottery_data():

    try:
        df = pd.read_csv(DATA_URL)

    except Exception:
        # fallback if internet unavailable
        df = pd.read_csv("data/raw/powerball_history.csv")

    return df
