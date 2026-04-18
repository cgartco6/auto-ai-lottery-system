import pandas as pd
import os
from utils.logger import get_logger

log = get_logger("HELPERS")

DATA_PATH = "data/processed/clean.csv"

def help_load():
    print("loading helper utilities")

def load_processed_data():

    try:

        if not os.path.exists(DATA_PATH):
            log.error("Processed dataset not found.")
            return None

        df = pd.read_csv(DATA_PATH)

        log.info(f"Loaded dataset: {df.shape}")

        return df

    except Exception as e:

        log.error(f"Failed to load data: {str(e)}")

        return None
