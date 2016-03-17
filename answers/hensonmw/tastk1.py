#!/usr/bin/env python
# encoding: utf-8

"""
My 1st program for Assignment 15

Created by Michael Henson on 26 March 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import argparse
import glob
import os
import itertools


def askingforfiles():
    parser = argparse.ArgumentParser(
        description="Asking User to Provide the path to the directory for task1")
    parser.add_argument(
        "--input",
        required=True,
        help="Provide the the directory path to task1 ",
        type=str
    )
    return parser.parse_args()


def getfile(file2):

    with open(file2[0], 'r') as file1:
        with open(file2[1], 'r') as file2:
            chained = itertools.chain(file1, file2)
            print('\n Look a put the two files together \n')
            for line in chained:
                print(line)


def main():
    path = askingforfiles()
    my_files = glob.glob(os.path.join(path.input, "*.txt"))
    getfile(my_files)

if __name__ == '__main__':
    main()
