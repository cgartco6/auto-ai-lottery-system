import json

REGISTRY_FILE = "data/models/registry.json"

def save_model_version(name, version, metrics):

    try:
        with open(REGISTRY_FILE, "r") as f:
            registry = json.load(f)
    except:
        registry = {}

    registry[name] = {
        "version": version,
        "metrics": metrics
    }

    with open(REGISTRY_FILE, "w") as f:
        json.dump(registry, f, indent=2)
