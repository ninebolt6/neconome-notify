import configparser


class Config:
    def __init__(self, config_path: str) -> None:
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_target_url(self) -> str:
        return self.config["Settings"]["TARGET_URL"]

    def get_span_index(self) -> int:
        return int(self.config["Settings"]["SPAN_INDEX"])

    def get_alert_number(self) -> int:
        return int(self.config["Settings"]["ALERT_NUMBER"])

    def get_duration(self) -> int:
        return int(self.config["Settings"]["DURATION"])
