import yaml


class ConfigReader:
    def __init__(self, path="config.yaml"):
        with open(path, "r") as f:
            self.config = yaml.safe_load(f)

    def get_wait_timeout(self):
        return self.config["wait_timeout"]

    def get_browser_options(self):
        return self.config.get("browser", {})

    def get_home_page_url(self):
        return self.config["home_page_url"]

    def get_maximize(self):
        return self.config.get("browser", {}).get("maximize", False)

    def get_headless(self):
        return self.config.get("browser", {}).get("headless", False)

    def get_lang_map(self):
        return self.config.get("lang_map", {"russian"})
