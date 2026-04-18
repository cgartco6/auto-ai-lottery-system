import time
from pipeline.orchestrator import run_pipeline

def start_scheduler():

    while True:

        print("Running scheduled pipeline...")

        run_pipeline()

        time.sleep(86400)  # 24 hours
