#!/usr/bin/env python3

from collections import Counter

import pytest

from file_organiser import get_files, get_type, main, process_files


# Test main
def test_path(tmp_path):
    """Test main with a directory containing one file, expecting 1 file to be processed."""
    (tmp_path / "file1.txt").touch()
    amount = main([str(tmp_path)])

    assert amount == 1


def test_main_empty_dir(tmp_path):
    """Test main with an empty directory, should process 0 files."""
    amount = main([str(tmp_path)])
    assert amount == 0


def test_main_no_path(tmp_path, monkeypatch):
    """Test main with no path, which should default to the current directory."""
    monkeypatch.chdir(tmp_path)
    (tmp_path / "file1.txt").touch()
    amount = main([])
    assert amount == 1


def test_main_file_not_found():
    """Test main with a non-existent file path."""
    with pytest.raises(FileNotFoundError):
        main(["/non/existent/path"])


def test_not_dir(tmp_path):
    """Test main with a non-directory path."""
    file = tmp_path / "text.txt"
    file.touch()
    with pytest.raises(NotADirectoryError, match="is not a directory"):
        list(main([str(file)]))


def test_with_file(tmp_path):
    """Test main with a file path."""
    fake_jpeg = tmp_path / "test.jpg"
    fake_jpeg.write_bytes(b"\xff\xd8\xff\xe0")
    file_type = main(["--file", str(fake_jpeg)])
    assert file_type == "image/jpeg"


# Test get_files
def test_file_not_found(tmp_path):
    """Test get_files with a non-existent file path."""
    with pytest.raises(FileNotFoundError, match="does not exist"):
        list(get_files(tmp_path / "not-here"))


def test_get_files_recursive(tmp_path):
    """Test get_files with recursive mode enabled."""
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
    """Test get_files with non-recursive mode enabled."""
    (tmp_path / "subdir1").mkdir()
    (tmp_path / "subdir2").mkdir()
    (tmp_path / "file1.txt").touch()
    (tmp_path / "subdir1" / "file2.jpg").touch()
    (tmp_path / "subdir2" / "file3.pdf").touch()

    # Test non-recursive behavior
    files = list(get_files(tmp_path, recursive=False))
    assert len(files) == 1
    assert tmp_path / "file1.txt" in files


def test_get_files_empty_dir(tmp_path):
    """Test get_files with an empty directory."""
    files = list(get_files(tmp_path))
    assert len(files) == 0


# Test process_files
def test_process_files_recursive(tmp_path):
    """Test process_files with recursive mode enabled."""
    # Create dummy files with different types
    (tmp_path / "file1.txt").write_text("hello")
    (tmp_path / "file2.jpg").touch()  # python-magic will likely identify this as empty data
    (tmp_path / "subdir").mkdir()
    (tmp_path / "subdir" / "file3.pdf").touch()

    counts = process_files(tmp_path)
    assert "text/plain" in counts
    assert counts["text/plain"] == 1


def test_process_files_non_recursive(tmp_path):
    """Test process_files with non-recursive mode enabled."""
    # Create dummy files
    (tmp_path / "file1.txt").write_text("hello")
    (tmp_path / "subdir").mkdir()
    (tmp_path / "subdir" / "file2.txt").write_text("world")

    counts = process_files(tmp_path, recursive=False)
    assert counts == Counter({"text/plain": 1})


# Test get_type
def test_get_type_image(tmp_path):
    """Test get_type with an image file."""
    fake_jpeg = tmp_path / "test.jpg"
    fake_jpeg.write_bytes(b"\xff\xd8\xff\xe0")
    type = get_type(str(fake_jpeg))
    assert type == "image/jpeg"


def test_get_type_with_temp_file(tmp_path):
    """Test get_type with a temporary file."""
    # Create a dummy txt file
    txt_content = b"This is a dummy text file."
    txt_file = tmp_path / "dummy.txt"
    with open(txt_file, "wb") as f:
        f.write(txt_content)
    # test with get_type
    type = get_type(txt_file)
    assert type == "text/plain"


def test_get_type_empty_file(tmp_path):
    """Test get_type with an empty file."""
    empty_file = tmp_path / "empty.dat"
    empty_file.touch()
    file_type = get_type(empty_file)
    assert file_type == "inode/x-empty"
