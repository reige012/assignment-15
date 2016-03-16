#!/usr/bin/env python
# encoding: utf-8

"""
Program takes a directory as input and then takes the two text files found in
the directory and sends them to a function that iterates over both of them,
line by line, at the same time. Each of the lines from both files are printed
to the screen in succession.

Edited by Alicia Reigel. 15 March 2016.
Copyright Alicia Reigel. Louisiana State University. 15 March 2016. All
rights reserved.

"""


import itertools
import glob
import os
import argparse


def parser_directorypath():
    """Collects the path of the directory where your files are"""
    parser = argparse.ArgumentParser(
        description="""Input the full path to the directory of interest"""
        )
    parser.add_argument(
            '--directorypath',
            required=True,
            type=str,
            help='Enter the path to the directory of interest.'
        )
    return parser.parse_args()


def opening_files_making_list(file1, file2):
    """opens both files and reads them line by line simultaneously. Prints to screen"""
    for file1_line, file2_line in itertools.zip_longest(open(file1), open(file2)):
        print(file1_line, file2_line)


def main():
    args = parser_directorypath()
    path_name = os.path.join(args.directorypath, "*.txt")
    # finds the pathnames for any files that have *c-darwin* in the directory
    file_path_list = glob.glob(path_name)
    # creates a list of the path names associated with the c-darwin files found
    file1 = os.path.basename(file_path_list[0])
    # finds the basename for the first file path in the list created by glob
    file2 = os.path.basename(file_path_list[1])
    # finds the basename of the second file path in the list created by glob
    os.chdir(args.directorypath)
    # changes the directory to the one input by argparse
    opening_files_making_list(file1, file2)


if __name__ == '__main__':
    main()
