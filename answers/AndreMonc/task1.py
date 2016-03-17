# !/usr/bin/env python
# encoding: utf-8


"""
My file iteration program
Created by Andre Moncrieff on 16 March 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
This code is based on Peter Sutton's code at the bottom of the
following page:
http://stackoverflow.com/questions/24960996/python-iterating-through-two-files-by-line-at-the-same-time

"""


import argparse
import os
import glob
import itertools


def parser():
    """
    Create argument input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", required=True,
                        help="Enter dir path for task1 files", type=str)
    args = parser.parse_args()
    return args


def list_of_filenames(directory_path):
    os.chdir(directory_path)
    list_of_filenames = glob.glob("*.txt")
    return list_of_filenames


def iterate_over_files(directory_path, filenames):
    os.chdir(directory_path)
    file_objects = []
    for item in filenames:
        file_objects.append(open(item, "r"))
    for lines in itertools.zip_longest(*file_objects, fillvalue=None):
            print(lines)


def main():
    args = parser()
    list_o_filenames = list_of_filenames(args.dir)
    iterate_over_files(args.dir, list_o_filenames)

if __name__ == '__main__':
    main()
