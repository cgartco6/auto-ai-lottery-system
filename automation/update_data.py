from pipeline.fetch_data import fetch_lottery_data

def run():

    df = fetch_lottery_data()

    print("Updated dataset")
    print(len(df), "draws loaded")


if __name__ == "__main__":
    run()
