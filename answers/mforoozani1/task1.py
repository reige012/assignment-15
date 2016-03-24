#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task1 to write a program that iterates over the lines of the
two files in the task-1 directory
"""
from itertools import zip_longest
import argparse
import glob
import os


def get_parser():
    """
   using argparse to takes the list  as input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", help='directory to use', type=str)
    # parser.add_argument("--inputfile2", required=True)
    args = parser.parse_args()

    return args


def iterate_overlines(inputfile1, inputfile2):
    """
use zip_longest in python 3 or izip in python 2 to print items in two arguments
at the same time
    """
    for line_file_1, line_file_2 in zip_longest(inputfile1, inputfile2):
        print(line_file_1, line_file_2)


def main():
    args = get_parser()
    file1 = glob.glob(os.path.join(args.directory, "*.txt"))
    print(file1)
    with open(file1[0], "r") as inputfile1, open(file1[1], "r") as inputfile2:
        # inputfile_string1 = inputfile1.read()
        # inputfile_string2 = inputfile2.read()
        iterate_overlines(inputfile1, inputfile2)


if __name__ == '__main__':
    main()
