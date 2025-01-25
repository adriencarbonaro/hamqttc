import os
import yaml

def setup_default_config(config_file):
    default_config = {
        'mqtt': {
            'host': 'localhost',
            'port': 1883,
            'username': 'YOUR_USERNAME',
            'password': 'YOUR_PASS',
        },
        'scripts_dir': os.path.expanduser("~/.config/hamqttc/scripts")
    }

    os.makedirs(os.path.dirname(config_file), exist_ok=True)
    os.makedirs(default_config['scripts_dir'], exist_ok=True)

    with open(config_file, 'w') as f:
        yaml.dump(default_config, f)


def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)
