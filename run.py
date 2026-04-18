from pipeline.fetch_data import fetch
from pipeline.clean_data import clean
from pipeline.features import build_features
from pipeline.train import train_models
from pipeline.simulate import run_simulation
from pipeline.generate import create_predictions
from telegram.bot import send_update

def main():

    fetch()
    clean()
    build_features()
    train_models()
    results = run_simulation()
    preds = create_predictions(results)
    send_update(preds)

if __name__ == "__main__":
    main()
