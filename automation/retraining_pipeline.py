from pipeline.fetch_data import fetch_lottery_data
from pipeline.generate_predictions import generate

def retrain():

    df = fetch_lottery_data()

    top13, top6 = generate()

    print("Top 6 predictions:")
    print(top6)

    print("Top 13 pool:")
    print(top13)


if __name__ == "__main__":
    retrain()
