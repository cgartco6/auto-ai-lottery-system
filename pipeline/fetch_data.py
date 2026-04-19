import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://www.nationallottery.co.za/results/powerball"


def fetch_lottery_data():

    r = requests.get(URL, timeout=30)
    soup = BeautifulSoup(r.text, "html.parser")

    draws = []

    rows = soup.select(".resultsTable tr")

    for row in rows[1:]:

        cols = row.text.strip().split()

        try:
            draw = {
                "date": cols[0],
                "n1": int(cols[1]),
                "n2": int(cols[2]),
                "n3": int(cols[3]),
                "n4": int(cols[4]),
                "n5": int(cols[5]),
                "pb": int(cols[6])
            }

            draws.append(draw)

        except:
            continue

    df = pd.DataFrame(draws)

    df.to_csv("data/raw/powerball_history.csv", index=False)

    return df
