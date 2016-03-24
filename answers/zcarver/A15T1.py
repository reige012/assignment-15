#! /usr/bin/env python
# encoding UTF-8

'''
Assignment15Task1 biol7800
ZacCarver 03/17/2016
Takes directory input and iterates over both files...albeit prints in a
columnar format...
'''

import os
import glob
import itertools
import argparse


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str,
                        help="provide a path to a couple of files")
    return parser.parse_args()


def combo(f1, f2):
    for l1, l2 in itertools.izip(open(f1).read(), open(f2).read()):
        l1 = l1.strip()
        l2 = l2.strip()
        print('{0}, {1}'.format(l1, l2))


def main():
    arg = args()
    files = glob.glob(os.path.join(arg.directory, '*.txt'))
    f1 = files[0]
    f2 = files[1]
    combo(f1, f2)

if __name__ == '__main__':
    main()
