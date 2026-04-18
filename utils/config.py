import yaml
import os

CONFIG_PATH = "config.yaml"

def load_config(path: str = CONFIG_PATH):

    if not os.path.exists(path):
        raise FileNotFoundError(f"Config not found: {path}")

    with open(path, "r") as f:
        return yaml.safe_load(f)


config = load_config()
