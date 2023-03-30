import argparse
from pathlib import Path

import yaml


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="the .yml user input file")
    args = parser.parse_args()
    input_file_str = args.input_file
    input_file = Path(input_file_str)
    time_all = run_and_time_all_code(input_file)
