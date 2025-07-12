import yaml


class ConfigReader:
    PATH_CONFIG = "config.yaml"

    def __init__(self, path=PATH_CONFIG):
        with open(path, "r") as f:
            self.config = yaml.safe_load(f)
