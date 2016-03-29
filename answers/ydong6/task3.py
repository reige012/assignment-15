#!/usr/bin/env python
# encoding: utf-8
'''
Created on Mar 17, 2016
Task 3
Generalize the program you wrote above to take an arbitrary start and stop date
and compute the number of weekend days between those two times (inclusive). Use
argparse to take the start and end times on the command line, and make sure that
you make it clear for the user exactly how they are supposed to enter these
start and stop dates. Your program should contain a main loop and an ifmain
statement, and it should be formatted correctly. You should run a linter against
your code to make sure you have formatted it according to PEP8.
@author: York
'''
import argparse
import datetime


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--d1' , help="Begin day,Type in the form as 2016/03/16" , type=str)
    parser.add_argument('--d2' , help="Last day,Type in the form as 2016/03/16" , type=str)
    return parser.parse_args()


def amount_weekends(d1 , d2):
    dura = d1
    counter = 0
    while d2 != d1:
        d2 -= datetime.timedelta(1)  #-1 if d2 is larger than d1
        if dura.weekday() == 5:  #or use isoweekday()
            counter += 1
        elif dura.weekday() == 6:  #Return the day of the week as an integer, where Monday is 0 and Sunday is 6
            counter += 1
        dura += datetime.timedelta(1)  #A timedelta object represents the difference between two dates or times.
    return counter


def main():
    arg = get_args()
    d1 = arg.d1.split('/')
    print(d1)
    d2 = arg.d2.split('/')
    day1 = datetime.date(int(d1[0]), int(d1[1]), int(d1[2]))
    day2 = datetime.date(int(d2[0]), int(d2[1]), int(d2[2]))
    weekends = amount_weekends(day1, day2)
    print("The total weekends between {} and {} is {} days.".format(day1, day2 , weekends))


if __name__ == '__main__':
    main()
