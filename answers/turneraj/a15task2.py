#!/usr/bin/env python
# encoding: utf-8

"""
 My second task for Assignment 15. Using datetime module to write a program
 count how many weekends are from now until the end of 2016.

 Created by A.J. Turner on March 17, 2016.
"""

import datetime


def weekends():
    """getting weekend days until Dec 31, 2016"""
    rightmeow = datetime.date(2016, 3, 17)
    yearend = datetime.date(2016, 12, 31)
    daydiff = datetime.timedelta(1)
    days = 0
    while yearend != rightmeow:
        yearend -= daydiff  # iterating by sub 1 from end date
        if yearend.isoweekday() in (6, 7):  # checking for sat/sunday
            days += 1  # if sat/sunday, add one
        print(days)


def main():
    weekends()


if __name__ == '__main__':
    main()
