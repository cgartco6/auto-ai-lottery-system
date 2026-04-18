from pipeline.orchestrator import run_pipeline
from core.logger import get_logger

log = get_logger("MAIN")

def main():

    log.info("Starting AI Simulation Cluster System")

    results = run_pipeline()

    log.info("Pipeline completed successfully")

    print("\nFINAL OUTPUT:")
    print(results)

if __name__ == "__main__":
    main()
