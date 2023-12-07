"""
    Format Check:
        - Black
        - Pylint
"""

import subprocess

from argparse import ArgumentParser


def _get_arguments():
    """
    Get command line arguments.
    """
    parser = ArgumentParser(description="Checker commands.")
    parser.add_argument("--path", "-p", help="Path to run the checker", default=".")

    return parser.parse_args()


def format_code_with_black(file_path):
    """
    Run Black
    """
    print("Running Black...")
    try:
        subprocess.run(["black", file_path], check=True)
        print(f"  Code formatting successful for {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"  Error formatting code: {e}")
    print()


def run_pylint(file_path):
    """
    Run pylint
    """
    print("Running pylint...")
    try:
        subprocess.run(["pylint", file_path], check=True)
        print(f"Pylint analysis successful for {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running Pylint: {e}")
    print()


def main():
    """
    Main function
    """
    arguments = _get_arguments()
    format_code_with_black(arguments.path)
    run_pylint(arguments.path)


if __name__ == "__main__":
    main()
