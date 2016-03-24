#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
14 March 2016
Assignment 15 Task 1

Using the `itertools`, `glob`, and `os` package, write a program that
iterates over the lines of the two files in the task-1 directory, simultaneously.
'''

import argparse
import os
import glob
import itertools


def itr_two_files():
    os.chdir('assignment-15/task1-files')
    file_list = glob.glob('*.*')
    with open(file_list[0]) as f1, open(file_list[1]) as f2:
        for line in itertools.chain(f2, f1):
            print(line[::-1]) # It would be cool to make one line read forward and one read backwards


def main():
    itr_two_files()


if __name__ == '__main__':
    main()
