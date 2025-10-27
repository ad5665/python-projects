#!/usr/bin/env python3

from pathlib import Path
from rich import print
from rich.progress import track
from collections import Counter
import magic

def get_type(file):
    type = magic.from_file(file, mime=True)
    return type

def get_files(path: str):
    p = Path(path)

    if not p.is_dir():
        f = get_type(path)
        return print(f"{path} is not a directory, it's a {f}")
    
    print(f"{path} is a valid dir")
    for dirpath, subdirs, files in p.walk():
        for f in files:
            yield dirpath / f

def process_files(path: str):
    count = Counter()
    for f in track(get_files(path), description="Working...."):
        count[get_type(f)] += 1
    print(count)


process_files("/mnt/c/Users/Adam/Desktop/adhd")
