# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 15
Oscar Johnson 16 March 2016
"""

import argparse
import glob
import os


def get_args():
    parser = argparse.ArgumentParser(
            description="""provide working directory for text files""")
    parser.add_argument('--input_dir',
                        type=str,
                        required=True,
                        help="enter a directory containing two text files",
                        )
    return parser.parse_args()


def file_reader(file):
    """takes directory containing two text files,
    does work on both files in that directory"""
    # filenames = glob.glob(os.path.join(path, "*.txt"))
    with open(file, 'r') as my_file:
        for line in my_file:
            print(line)


def main():
    args = get_args()
    filenames = glob.glob(os.path.join(args.input_dir, "*.txt"))
    result = map(file_reader, filenames)
    # file_reader(args.input_dir)
    print(list(result))

if __name__ == '__main__':
    main()
