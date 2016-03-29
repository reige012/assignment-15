#! usr/bin/env python
# encoding: utf-8

"""
Assignment 15
Task 1 Program: Iterating over 2 files simultaneously
Jessie Salter
16 March 2016
"""

import argparse
import itertools
import glob
import os


def parser():
    '''Takes user input'''
    parser = argparse.ArgumentParser(
        description='''Gets the paths of the input and output files.'''
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Enter the path to the directory you want to work from.",
        type=str
    )
    return parser.parse_args()


def iter_print(file1, file2):
    '''Uses the zip_longest module of itertools to simultaneously read two
    files and print each line to the screen.'''
    # Adapted from:
    # http://stackoverflow.com/questions/11295171/read-two-textfile-line-by-line-simultaneously-python
    with open(file1, 'r') as file1, open(file2, 'r') as file2:
        for line, ligne in itertools.zip_longest(file1, file2):
            print('{:<30}{:<30}'.format(line.strip(), ligne.strip()))


def main():
    args = parser()
    if args.input[-1] != '/':
        path_input = args.input + '/'
    else:
        path_input = args.input
    files = []
    for filename in glob.glob(os.path.join(path_input, '*.txt')):
        files.append(filename)
    iter_print(files[0], files[1])

if __name__ == '__main__':
    main()
