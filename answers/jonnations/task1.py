#!/usr/bin/env python
# utf-8

"""
Assignment 15, Task 1
Jon Nations on 15 March 2016
This program iterates over two files simultaneously.

"""


import argparse
import glob
import os
import itertools


def file_in():
    """gets input directory containint text files"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', required=True, type=str,
                        help="give input directory where the text files are stored")
    # parser.add_argument('--output', required=True, help='give output file')
    return parser.parse_args()


def file_1(my_files):
    with open(my_files[0], 'r') as clean:
        clean = clean.read()
        file1 = clean.split('\n')
        #file1 = clean.read()
        # print(type(file1))
        return file1


def file_2(my_files):
    with open(my_files[1], 'r') as clean:
        clean = clean.read()
        file2 = clean.split('\n')
        # print(file2)
        return file2


def main():
    file_in()
    args = file_in()
    my_files = glob.glob(os.path.join(args.directory, "*.txt"))
    # I am assuming this produces a list of files called "my_files"
    file1 = file_1(my_files)
    file2 = file_2(my_files)
    for f1, f2 in itertools.zip_longest(file1, file2):
        print(f1, '|', f2)

if __name__ == '__main__':
    main()
