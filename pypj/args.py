import argparse
import sys

from .const import HELP


def args() -> None:
    parser = argparse.ArgumentParser(description="Modern python project builder")
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    args = parser.parse_args()
    if args.version:
        print(HELP)
        sys.exit(0)
