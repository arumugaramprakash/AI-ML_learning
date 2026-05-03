#!/usr/bin/env python3

import os

def recursive_read_directory(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"Directory: {dirpath}")
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            print(f"  File: {filepath}")

if __name__ == "__main__":
    root_directory = "."
    recursive_read_directory(root_directory)
