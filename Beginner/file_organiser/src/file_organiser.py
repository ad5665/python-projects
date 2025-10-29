#!/usr/bin/env python3

import argparse
import os
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
def process_files(path: Path | str, recursive=False):
    counts = Counter()
    for f in track(get_files(path, recursive), description="Working...."):
        counts[get_type(f)] += 1
    return counts


def parse_args(argv=None):
    ap = argparse.ArgumentParser(
        prog="File Organiser", description="Scans a dir and presents types of files"
    )
    ap.add_argument(
        "dir",
        type=Path,
        nargs="?",
        default=os.getcwd(),
        help="Provide a Windows or Unix directory path, default is working directory",
    )
    ap.add_argument("-f", "--file", type=Path, help="Provide a Windows or Unix file path")
    ap.add_argument(
        "-n",
        "--no-recursive",
        action="store_true",
        help="(future) disable recursion if you add non-recursive mode",
    )
    ap.add_argument("--list", action="store_true", help="(future) list files with detected MIME")
    return ap.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    print(args)
    if args.file:
        print(f"[bold cyan]The file {args.file} is a [yellow]{get_type(args.file)}")
    else:
        counts = process_files(args.dir, args.no_recursive)
        print(f"[bold cyan]{counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
