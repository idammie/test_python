"""Project configuration"""

import os
from pathlib import Path

from .utils import yaml_load

# --------------------------------------------------------------------------- #
# Load secure variables from .env file
# --------------------------------------------------------------------------- #

# for .env file in USER directory
# user_dir = C:\\USERS\\<<firstname.lastname>>
# user_dir = os.path.join(os.path.expanduser("~"))
# dotenv_path = os.path.join(user_dir, ".env")
# print(dotenv_path)
# load_dotenv(dotenv_path)

# path to yaml project configuration file
project_root = Path(__file__).parents[1]


# --------------------------------------------------------------------------- #
def load_catalog():
    catalog = os.path.join(project_root, "config/catalog.yaml")
    with open(catalog, "r") as f:
        catalog = yaml_load(f)

    return catalog


def load_parameters():
    parameters = os.path.join(project_root, "config/parameters.yaml")
    with open(parameters, "r") as f:
        parameters = yaml_load(f)
    return parameters


# --------------------------------------------------------------------------- #

if __name__ == "__main__":
    # load catalog
    print("Loading catalog...")
    catalog = load_catalog()
    parameters = load_parameters()
    print(catalog["test"]["filepath"])
