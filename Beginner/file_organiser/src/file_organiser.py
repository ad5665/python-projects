#!/usr/bin/env python3

import argparse
from collections import Counter
from pathlib import Path

import magic
from rich import print
from rich.progress import track


# Using python-magic, determine what type of file is passed
def get_type(file_path: Path | str) -> str:
    try:
        return magic.from_file(file_path, mime=True)
    except Exception:
        return print(f"Failed to generate type of file for {file_path}")


# Using a path, return all files, using full Path and filename from Path.Walk()
def get_files(path: Path | str, recursive=False):
    p = Path(path)

    if not p.exists():  # If the path doesn't exist, throw a error
        raise FileNotFoundError(f"{path} does not exist")
    if not p.is_dir():  # If not a dir, catpure file type and throw a error
        f = get_type(path)
        raise NotADirectoryError(f"{path} is not a directory, it's a {f}")

    print(f"[yellow][u]{p}[/u] [green]is a valid dir")
    for dirpath, subdirs, files in p.walk():
        for f in files:
            yield dirpath / f
        if recursive:
            break


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
    parser.add_argument("dir", type=str, help="Provide a Windows or Unix directory path")

    args = parser.parse_args()

    # Call Process files with the suppiled argument
    process_files(args.dir)
