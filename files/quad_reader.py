"""This module processes a simple yml file.

Example:
# activate the atmesh virtual environment
~/autotwin/lessons> source .venv/bin/activate.fish
(.venv) ~/autotwin/lessons> cd files
(.venv) python quad_reader.py two_quads.yml
"""


import argparse
from pathlib import Path

import yaml


def contents(input_file: Path):
    print(f"This module is {Path(__file__).resolve()}\n")

    fin = Path(input_file).expanduser()

    if not fin.is_file():
        raise FileNotFoundError(f"File not found: {str(fin)}")

    file_type = input_file.suffix.casefold()

    supported_types = (".yaml", ".yml")

    if file_type not in supported_types:
        raise TypeError("Only file types .yaml, and .yml are supported.")

    try:
        with open(input_file, "r") as stream:
            # See deprecation warning for plain yaml.load(input) at
            # https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
            db = yaml.load(stream, Loader=yaml.SafeLoader)
    except yaml.YAMLError as error:
        print(f"Error with YAML file: {error}")
        # print(f"Could not open: {self.self.path_file_in}")
        print(f"Could not open or decode: {input_file}")
        # raise yaml.YAMLError
        raise OSError

    keys = db.keys()

    # breakpoint()

    for item in keys:
        print(f"key: {item}")
        print(f"value: {db[item]}\n")


def main():
    """Runs the module from the command line."""
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="the .yml user input file")
    args = parser.parse_args()
    input_file = Path(args.input_file).expanduser()
    contents(input_file=input_file)


if __name__ == "__main__":
    main()
