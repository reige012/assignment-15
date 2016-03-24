#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:49:24 2016

@author: Glaucia
"""

import argparse

import glob

import os

import itertools


def arguments():
    """Parsing arguments to have input file"""
    parser = argparse.ArgumentParser(description="""my argument parser""")
    parser.add_argument('directory_name', type=str, help="""give the entire name of the directory
                        (and path) containing your files""")
    args = parser.parse_args()
    directory_name = args.directory_name
    return directory_name


def getting_files(input_directory):
    """Gets a list with the names of the files contatining the sentences
       I will print"""
    list_files = []
    for filename in glob.glob(os.path.join(input_directory + "/*.txt")):
        list_files.append(filename)
    return list_files


def reading_files(list_files):
    """Reads two files and prints their sentences simultaneously"""
    with open(list_files[0]) as file1, open(list_files[1]) as file2:
        for line1, line2 in itertools.zip_longest(file1, file2):
            print("{0}{1}".format(line1, line2))


def main():
    arg = arguments()
    file1_file2 = getting_files(arg)
    reading_files(file1_file2)


if __name__ == '__main__':
    main()
