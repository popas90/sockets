"""
Usage: python unwind_storage.py [username_folder_path]

The script scans the username_folder_path recursively and finds all files, then
pieces them back together by reading the sqlite database. The expected
folder structure for this script is the one generated by initialize_storage.py.

The output will be a folder named like the input, but containing the exact
folder tree like before running the initialize script.
"""
