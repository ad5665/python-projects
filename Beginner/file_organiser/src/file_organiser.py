#!/usr/bin/env python3

import argparse
from collections import Counter
from pathlib import Path

import magic
from rich import print
from rich.progress import track


# Using python-magic, determine what type of file is passed
def get_type(file_path: Path | str) -> str:
    return magic.from_file(file_path, mime=True)


# Using a path, return all files, using full Path and filename from Path.Walk()
def get_files(path: Path | str, recursive=True):
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
        if not recursive:
            break


# This fuction calls the above 2 fuctions, to grab a list of files, and then fetching the file types, saving within a Counter
def process_files(path: Path | str, recursive=True):
    counts: Counter[str] = Counter()
    for f in track(get_files(path, recursive), description="Working...."):
        try:
            file_type = get_type(f)
        except Exception:
            print(f"[red]Failed to generate type of file for {f}")
            continue
        counts[file_type] += 1
    return counts


def parse_args(argv=None):
    ap = argparse.ArgumentParser(
        prog="File Organiser", description="Scans a dir and presents types of files"
    )
    ap.add_argument(
        "dir",
        type=Path,
        nargs="?",
        default=Path.cwd(),
        help="Provide a Windows or Unix directory path, default is working directory",
    )
    ap.add_argument("-f", "--file", type=Path, help="Provide a Windows or Unix file path")
    ap.add_argument(
        "-n",
        "--no-recursive",
        action="store_false",
        help="Disable recursion if you add non-recursive mode",
    )
    ap.add_argument("--list", action="store_true", help="(future) list files with detected MIME")
    return ap.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if args.file:
        file_type = get_type(args.file)
        print(f"[bold cyan]The file {args.file} is a [yellow]{file_type}")
        return file_type
    else:
        counts = process_files(args.dir, args.no_recursive)
        print(f"[bold cyan]{counts}[/bold cyan]")
        return counts.total()


if __name__ == "__main__":
    raise SystemExit(main())
