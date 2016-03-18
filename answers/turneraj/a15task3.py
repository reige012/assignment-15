#!/usr/bin/env python
# encoding: utf-8

"""
 My third task for Assignment 15. Using datetime module to write a
 program count how many weekends are from now until the end of 2016.

 Created by A.J. Turner on March 17, 2016.
"""

import argparse
import datetime


def get_date():
    """"user to input working directory"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--startdate", help="Enter starting date: \
    Year/M/D", type=str)
    parser.add_argument("--enddate", help="Enter end date: \
    Year/MM/DD", type=str)
    args = parser.parse_args()
    return args


def weekends(startdate, enddate):
    """getting weekend days until Dec 31, 2016"""
    start = startdate.replace("/", ", ")
    end = enddate.replace("/", ", ")
    rightmeow = datetime.datetime.strptime(start, "%Y, %m, %d")
    yearend = datetime.datetime.strptime(end, "%Y, %m, %d")
    daydiff = datetime.timedelta(1)
    days = 0
    while yearend != rightmeow:
        yearend -= daydiff  # iterating by sub 1 from end date
        if yearend.isoweekday() in (6, 7):  # checking for sat/sunday
            days += 1  # if sat/sunday, add one
    print("{} weekend days".format(days))


def main():
    args = get_date()
    weekends(args.startdate, args.enddate)


if __name__ == '__main__':
    main()
