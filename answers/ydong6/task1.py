#!/usr/bin/env python
# encoding: utf-8
'''
Created on Mar 16, 2016
Task 1
When working with sequence data, you often need to iterate over two files at the
same time (think of iterating over Read 1 and Read 2 fastq files
simultaneously). Using the itertools, glob, and os package, write a program that
iterates over the lines of the two files in the task-1 directory,
simultaneously. Your program should contain a main loop and an ifmain statement,
and it should be formatted correctly. You should run a linter against your code
to make sure you have formatted it according to PEP8. 
@author: York
'''
import argparse
import os
from itertools import zip_longest
import glob


def dir_file(filepath):
    filepath.add_argument("--dir",required=True,type=str,help='Enter the directory of the file')
    

def iterate(file1, file2):
    with open(file1, 'r') as file1:
        with open(file2, 'r') as file2:
            for file_1, file_2 in zip_longest(file1, file2):
                print('{}\n{}'.format(file_1,file_2))


def main():
    dir_parser = argparse.ArgumentParser()
    dir_file(dir_parser)
    path_args = dir_parser.parse_args()
    os.chdir(path_args.dir)
    files = glob.glob('*.txt')
    iterate(files[0], files[1])
    
    
if __name__ == '__main__':
    main()