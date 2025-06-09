import yaml
import os

def load_config(file_name="config.yaml"):
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, '..', 'config', file_name)
    config_path = os.path.abspath(config_path)

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at: {config_path}")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config
