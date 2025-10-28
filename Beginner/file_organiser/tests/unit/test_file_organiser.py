#!/usr/bin/env python3

import pytest

from file_organiser import get_files, get_type, process_files


def test_path():
    amount = process_files("/mnt/c/Users/Adam/Desktop/adhd/").total()
    assert amount > 0


def test_not_dir():
    with pytest.raises(NotADirectoryError, match="is not a directory"):
        list(get_files("/tmp/file-org/text.txt"))


def test_get_image():
    type = get_type("/mnt/c/Users/Adam/Desktop/adhd/20250820_160657.jpg")
    assert type == "image/jpeg"
