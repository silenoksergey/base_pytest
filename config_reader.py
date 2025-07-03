import yaml


class ConfigReader:
    def __init__(self, path="config.yaml"):
        with open(path, "r") as f:
            self.config = yaml.safe_load(f)

    def __getitem__(self, item):
        return self.config[item]
