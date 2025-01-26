import os
import yaml
from getpass import getpass as inputPassword
from log import Log

DEFAULT_SCRIPTS_DIR = "scripts"
DEFAULT_LOG_FILE = "~/.local/share/hamqttc/logs/hamqttc.log"

class Config:
    def __init__(self, log: Log):
        self.logger = log

    def getMqttCredentials(self):
        mqtt_host = input("Enter MQTT Hostname: ")
        mqtt_port = input("Enter MQTT Port: ")
        mqtt_username = input("Enter MQTT Username: ")
        mqtt_password = inputPassword("Enter MQTT Password: ")

        return {
            'mqtt_config': {
                'host': mqtt_host,
                'port': mqtt_port,
                'username': mqtt_username,
                'password': mqtt_password
            }
        }

    def load(self, config_file):
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)

    def check(self, config_file: str):
        if not os.path.exists(config_file):
            config_dir = os.path.dirname(config_file)
            self.logger.log(f"Creating config directory {config_dir}")
            os.makedirs(config_dir, exist_ok=True)
            mqtt_credentials = self.getMqttCredentials()

            # Scripts
            os.makedirs(os.path.join(config_dir, DEFAULT_SCRIPTS_DIR), exist_ok=True)
            mqtt_credentials['scripts_dir'] = os.path.join(config_dir, DEFAULT_SCRIPTS_DIR)

            # Logs
            log_file = os.path.expanduser(DEFAULT_LOG_FILE)
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            mqtt_credentials['log_file'] = log_file

            self.logger.log(f"Writing config in {config_file}")
            with open(config_file, 'w') as f:
                yaml.dump(mqtt_credentials, f, default_flow_style=False)
