#!/usr/bin/env python
# encoding: utf-8

"""
 My first task for Assignment 15.

 Created by A.J. Turner on March 17, 2016.
"""

import itertools
import glob
import os
import argparse


def get_location():
    """"user to input working directory"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--in_directory", help="Path to input directory", type=str)
    args = parser.parse_args()
    return args


def getstuff(files_in):
    with open(files_in[0], "r") as myfile1:
        with open(files_in[1], "r") as myfile2:
            together = itertools.chain(myfile1, myfile2)
            for shit in together:
                print(shit)


def main():
    args = get_location()
    files_in = glob.glob(os.path.join(args.in_directory, "*.txt"))
    print(list(files_in))
    getstuff(files_in)


if __name__ == '__main__':
    main()
