
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Author: Marco
# @Date:   2016-03-15 15:51:53
# @Last Modified by:   Admin123
# @Last Modified time: 2016-03-15 18:34:12

import os
import argparse
import itertools
import glob
import operator


def my_parser():
    '''
    Function to parse arguments from the terminal
    '''
    parser = argparse.ArgumentParser(description="""This is the argument
                                     parser""")
    parser.add_argument('in_folder', type=str, help='type the name of the'
                        ' folder you would like to get the txt files to '
                        'count words')
    args = parser.parse_args()
    inp = args.in_folder
    return inp


def open_file(in_path):
    with open(in_path, 'r') as fil:
        my_list = fil.readlines()
        result = list(map(operator.methodcaller("replace", "\n", ""), my_list))
    return result


def main():
    inp = my_parser()
    folder_files = glob.glob(inp+'\*.txt')
    my = list(map(open_file, folder_files))
    print("\nTHESE ARE THE LINES IN MY FILES\n")
    for fil in itertools.zip_longest(my[0], my[1]):
        print("{:23} | {:30}".format(fil[0], fil[1]))
    os.chdir(inp)
    check = os.getcwd()
    print("\nYou read the files in folder '{}'".format(check))

if __name__ == '__main__':
    main()
