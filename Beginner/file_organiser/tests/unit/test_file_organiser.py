#!/usr/bin/env python3

import pytest

from file_organiser import main, get_files, get_type, process_files


# Test main with args
def test_path():
    amount = main(["/mnt/c/Users/Adam/Desktop/adhd/"]).total()
    assert amount > 0


def test_no_path():
    amount = main().total()
    assert amount > 0


def test_not_dir():
    with pytest.raises(NotADirectoryError, match="is not a directory"):
        list(main(["/tmp/file-org/text.txt"]))


def test_with_file():
    file_type = main(["--file", "/mnt/c/Users/Adam/Desktop/adhd/20250820_160657.jpg"])
    assert file_type == "image/jpeg"


# Test get_files


# Test get_type
def test_get_type_image():
    type = get_type("/mnt/c/Users/Adam/Desktop/adhd/20250820_160657.jpg")
    assert type == "image/jpeg"


def test_get_type_exception():
    result = get_type(
        "home/acharlton/Documents/git/mine/python-projects/Beginner/file_organiser/.venv/lib64"
    )
    assert "Failed to generate type of file for" in result
