# File Organizer

Goal: Sort files in a directory by extension (like photos → /images, .txt → /docs).
Why it’s good: Practice with os, shutil, and command-line args (argparse).
Tests: Use pytest’s tmp_path fixture to verify the files get moved to the right spot.


### shutil
The shutil module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal. For operations on individual files, see also the os module.


### os
This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see open(), if you want to manipulate paths, see the os.path module, and if you want to read all the lines in all the files on the command line see the fileinput module. For creating temporary files and directories see the tempfile module, and for high-level file and directory handling see the shutil module.

### argparse
The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages. The module will also issue errors when users give the program invalid arguments.

