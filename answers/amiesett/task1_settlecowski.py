#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 15 Task 1

Amie Settlecowski
18 Mar. 2016

Iterates over 2 files simultaneously, printing each line to screen.
"""


import argparse
import os
import glob
import itertools


def get_args(parserr):
    '''
    Requires --dir flag for user to specify path to directory with input files
    '''
    parserr.add_argument("--dir",
        required=True,
        help="Path to directory with input files",
        type=str)


def files_by_line(file1, file2):
    '''Iterate through 2 specifed files, printing each line.'''
    with open(file1, 'r') as open_file1:
        with open(file2, 'r') as open_file2:
            for lines in itertools.zip_longest(open_file1, open_file2):
                processed_lines = list((l.rstrip().lstrip() for l in lines))
                print('{}\n{}'.format(processed_lines[0], processed_lines[1]))


def main():
    # creater Parser object with arguments for path to appropriate directory
    path_name_parser = argparse.ArgumentParser()
    get_args(path_name_parser)
    path_args = path_name_parser.parse_args()
    # change directory to appropriate directory
    os.chdir(path_args.dir)
    # collect all text files
    files = glob.glob('*.txt')
    files_by_line(files[0], files[1])
if __name__ == '__main__':
    main()
