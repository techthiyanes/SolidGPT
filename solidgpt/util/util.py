import json
import os
from definitions import *


def save_to_json(data, filename="data.json"):
    # Save data to a JSON file
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


def load_from_json(filename="data.json"):
    # Load data from a JSON file
    with open(filename, "r") as json_file:
        loaded_data = json.load(json_file)
    return loaded_data


def save_to_md(filename, content: str, path = "") -> str:
    path = os.path.join(ROOT_DIR, path)
    full_path = os.path.join(path, filename)
    with open(full_path, "w") as md_file:
        md_file.write(content)
    logging.info(f"Information saved to {full_path}")
    return full_path


def save_to_md2(filename, content: str) -> str:
    full_path = filename
    with open(full_path, "w") as md_file:
        md_file.write(content)
    logging.info(f"Information saved to {full_path}")
    return full_path