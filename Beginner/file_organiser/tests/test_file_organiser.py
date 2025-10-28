#!/usr/bin/env python3

import pytest
from ..file_organiser import process_files
from ..file_organiser import get_files


def test_path():
    amount = process_files("/mnt/c/Users/Adam/Desktop/adhd/").total()
    assert amount > 0

def test_not_dir():
    with pytest.raises(NotADirectoryError, match="is not a directory"):
        list(get_files("/tmp/file-org/text.txt"))