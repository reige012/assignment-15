# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 15
Oscar Johnson 16 March 2016
"""

import itertools
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


def file_reader(files):
    """takes directory containing two text files,
    does work on both files in that directory"""
    with open(files[0], 'r') as file1, open(files[1], 'r') as file2:
        for line1, line2 in zip(file1, file2):
            print(line1, line2)


def main():
    args = get_args()
    filenames = glob.glob(os.path.join(args.input_dir, "*.txt"))
    file_reader(filenames)
    # can't get these itertools to work...
    # result = itertools.starmap(file_reader, [filenames])
    # result = itertools.starmap(file_reader, [tuple(filenames)])
    # result = itertools.starmap(file_reader, [(filenames[0]), (filenames[1])])
    # print(list(result))

if __name__ == '__main__':
    main()
