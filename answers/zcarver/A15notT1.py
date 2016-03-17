#! /usr/bin/env python
# encoding UTF-8

'''
Assignment15Task1 biol7800
ZacCarver 03/17/2016
'''

import argparse
import glob
import itertools
import os
import re
import fileinput


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str,
                        help="provide a path to a couple of files")
    return parser.parse_args()


def wrt(files):
    #writing both files into one
    file = open('combofile3.txt', 'w')
    f3lines = fileinput.input(files)
    file.writelines(f3lines)
    #opens and reads the new file
    with open('combofile3.txt', 'r') as f3:
        combo_file = f3.read()
    return combo_file


def stringit(f3):
    txt = f3.lower()
    txt = re.sub(r'\W+', ' ', txt)
    f3_str = str(txt)
    return f3_str


def combinations(f3_str):
    '''iterates over the files by showing the total length of combinations
    between each element of every line of the file containing contents of both
    original files. I would not recomend printing the combinations made.'''
    #for a in itertools.combinations(f3_str, 2):
        #print(a)
    l_of_combos = len(list(itertools.combinations(f3_str, 2)))
    print(l_of_combos)


def main():
    arg = args()
    files = glob.glob(os.path.join(arg.directory, '*.txt'))
    os.chdir(arg.directory)
    combo_file = wrt(files)
    f3_str = stringit(combo_file)
    combinations(f3_str)

if __name__ == '__main__':
    main()
