#!/usr/bin/env python3

import pytest

from file_organiser import main, get_files, get_type, process_files


# Test main with args
def test_path():
    amount = main(["/mnt/c/Users/Adam/Desktop/adhd/"])
    assert amount > 0


def test_no_path():
    amount = main([])
    assert amount > 0


def test_no_path_recursive():
    amount = main(["--no-recursive"])
    assert amount > 0


def test_file_not_found():
    with pytest.raises(FileNotFoundError, match="does not exist"):
        list(get_files("/tmp/file-org/not-here"))


def test_not_dir():
    with pytest.raises(NotADirectoryError, match="is not a directory"):
        list(main(["/tmp/file-org/text.txt"]))


def test_with_file():
    file_type = main(["--file", "/mnt/c/Users/Adam/Desktop/adhd/20250820_160657.jpg"])
    assert file_type == "image/jpeg"


# Test get_files
def test_get_files_recursive(tmp_path):
    # Create a dummy directory structure
    (tmp_path / "subdir1").mkdir()
    (tmp_path / "subdir2").mkdir()
    (tmp_path / "file1.txt").touch()
    (tmp_path / "subdir1" / "file2.jpg").touch()
    (tmp_path / "subdir2" / "file3.pdf").touch()

    # Test recursive behavior (default)
    files = list(get_files(tmp_path))
    assert len(files) == 3
    assert tmp_path / "file1.txt" in files
    assert tmp_path / "subdir1" / "file2.jpg" in files
    assert tmp_path / "subdir2" / "file3.pdf" in files


def test_get_files_non_recursive(tmp_path):
    # Create a dummy directory structure
    (tmp_path / "subdir1").mkdir()
    (tmp_path / "subdir2").mkdir()
    (tmp_path / "file1.txt").touch()
    (tmp_path / "subdir1" / "file2.jpg").touch()
    (tmp_path / "subdir2" / "file3.pdf").touch()

    # Test non-recursive behavior
    files = list(get_files(tmp_path, recursive=True))
    assert len(files) == 1
    assert tmp_path / "file1.txt" in files


def test_process_files_recursive(tmp_path):
    # Create dummy files with different types
    (tmp_path / "file1.txt").write_text("hello")
    (tmp_path / "file2.jpg").touch()  # python-magic will likely identify this as empty data
    (tmp_path / "subdir").mkdir()
    (tmp_path / "subdir" / "file3.pdf").touch()

    counts = process_files(tmp_path)
    assert "text/plain" in counts
    assert counts["text/plain"] == 1


# Test get_type
def test_get_type_image():
    type = get_type("/mnt/c/Users/Adam/Desktop/adhd/20250820_160657.jpg")
    assert type == "image/jpeg"


def test_get_type_with_temp_file():
    # Create a dummy txt file
    txt_content = b"This is a dummy text file."
    txt_file = "/tmp/dummy.txt"
    with open(txt_file, "wb") as f:
        f.write(txt_content)
    # test with get_type
    type = get_type(txt_file)
    assert type == "text/plain"
