#!/usr/bin/env python3

import pytest
from ..file_organiser import process_files


def test_path():
    amount = process_files("/mnt/c/Users/Adam/Desktop/adhd/").total()
    assert  amount > 0