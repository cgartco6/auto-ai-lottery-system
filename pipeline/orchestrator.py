from pipeline.fetch_data import fetch_data
from pipeline.clean_data import clean_data
from pipeline.feature_engineering import build_features
from pipeline.train_models import train_models
from pipeline.simulation_engine import simulate
from pipeline.generate_outputs import generate

from core.logger import get_logger

log = get_logger("ORCHESTRATOR")

def run_pipeline():

    log.info("Step 1: Fetching data")
    fetch_data()

    log.info("Step 2: Cleaning data")
    clean_data()

    log.info("Step 3: Feature engineering")
    build_features()

    log.info("Step 4: Training models")
    train_models()

    log.info("Step 5: Running simulation")
    results = simulate()

    log.info("Step 6: Generating outputs")
    output = generate(results)

    return output
