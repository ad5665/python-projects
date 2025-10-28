#!/usr/bin/env python3

from pathlib import Path
from rich import print
from rich.progress import track
from collections import Counter
import magic
import argparse


# Using python-magic, determine what type of file is passed
def get_type(file):
    type = magic.from_file(file, mime=True)
    return type


# Using a path, return all files, using full Path and filename from Path.Walk()
def get_files(path: str):
    p = Path(path)

    if not p.is_dir():
        f = get_type(path)
        raise NotADirectoryError(f"{path} is not a directory, it's a {f}")

    print(f"[yellow][u]{path}[/u] [green]is a valid dir")
    for dirpath, subdirs, files in p.walk():
        for f in files:
            yield dirpath / f


# This fuction calls the above 2 fuctions, to grab a list of files, and then fetching the file types, saving within a Counter
def process_files(path: str):
    count = Counter()
    for f in track(get_files(path), description="Working...."):
        count[get_type(f)] += 1
    print(f"[bold cyan]{count}")
    return count


if __name__ == "__main__":
    # Define argument for dir
    parser = argparse.ArgumentParser(
        prog="File Organiser", description="Scans a dir and presents types of files"
    )
    parser.add_argument(
        "dir", type=str, help="Provide a Windows or Unix directory path"
    )

    args = parser.parse_args()

    # Call Process files with the suppiled argument
    process_files(args.dir)
