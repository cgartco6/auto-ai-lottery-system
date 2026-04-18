import pandas as pd
import numpy as np
from utils.logger import get_logger
from utils.helpers import load_processed_data
from models.frequency_model import frequency_model
from models.markov_model import markov_model
from models.bayesian_model import bayesian_update

log = get_logger("TRAIN")

def train_models():

    log.info("Loading dataset for training...")

    df = load_processed_data()

    if df is None or df.empty:
        log.error("No training data found.")
        return None

    data = df.values

    log.info("Training frequency model...")
    freq = frequency_model(data)

    log.info("Training Markov model...")
    markov = markov_model(data)

    log.info("Applying Bayesian adjustment...")
    bayes = bayesian_update(
        prior=freq,
        likelihood=np.mean(markov, axis=0)
    )

    log.info("Training complete.")

    np.save("data/models/frequency.npy", freq)
    np.save("data/models/markov.npy", markov)
    np.save("data/models/bayesian.npy", bayes)

    return {
        "frequency": freq,
        "markov": markov,
        "bayesian": bayes
    }
