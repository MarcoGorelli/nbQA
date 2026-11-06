"""Local module with subcommand."""

import argparse
import sys
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    """Print word (subcommand), ignore paths"""
    parser = argparse.ArgumentParser()
    parser.add_argument("word", nargs=1)
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args(argv)
    print(args.word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
