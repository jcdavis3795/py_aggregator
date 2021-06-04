from pathlib import Path
import os
import json

CONFIG_DIR = Path(os.path.expanduser('~/.py_aggregator'))
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')


def get_config():
    with open(CONFIG_FILE) as f:
        return json.loads(f.read())
