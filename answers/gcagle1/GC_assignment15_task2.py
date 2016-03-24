#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
14 March 2016
Assignment 15 Task 2
a program that determines, from now until the end of 2016,
how many weekend days there are.

Code adapted from my personal favorite stack overflow solution
due to clarity:
http://stackoverflow.com/a/3615634 by Coding District
I've adapted it to count weekends instead of weekdays.

weekend_finder2 adapted from http://stackoverflow.com/a/3615984 Dave Web
improvement by Paul McGuire
'''

import datetime
import numpy


def weekend_finder():
    today = datetime.date.today()
    end_of_yr = datetime.date(2016, 12, 31)
    delta = datetime.timedelta(1)
    days = 0
    while end_of_yr != today:
        end_of_yr -= delta
        if end_of_yr.isoweekday() not in (range(1, 6)):
            days += 1
    print(days/2)  # This gives the number of weekends, not days.


def weekend_finder2():
    fromdate = datetime.date.today()
    todate = datetime.date(2016, 12, 31)
    daygenerator = (fromdate + datetime.timedelta(x + 1) for x in range((todate - fromdate).days))
    print(sum(day.weekday() > 5 for day in daygenerator))


def main():
    weekend_finder()
    weekend_finder2()


if __name__ == '__main__':
    main()
