from utils.config_loader import load_config

class RuntimeConfig:

    def __init__(self):
        self.config = load_config()

    def get(self, key, default=None):
        return self.config.get(key, default)

config = RuntimeConfig()
