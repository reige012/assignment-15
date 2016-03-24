#!/usr/bin/env python
# encoding: utf-8
"""
assignment 15.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
from itertools import zip_longest
import glob
import os


def read_both_files():
    file_path = 'C:\\Users\\mukkucha\\Desktop\\7800 Biolprogramming\\assignment 15'
    open_file = glob.glob(os.path.join(file_path, '*.txt'))
    f1 = open(open_file[0], 'r')
    f2 = open(open_file[1], 'r')
    for line1, line2 in zip_longest(f1, f2):
        motif1 = line1.strip()
        motif2 = line2.strip()
        print("{0}\t{1}".format(motif1, motif2))


def main():
    read_both_files()


if __name__ == '__main__':
    main()
