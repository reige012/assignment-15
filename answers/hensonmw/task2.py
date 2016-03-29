#!/usr/bin/env python
# encoding: utf-8

"""
My 2nd program for Assignment 15

Created by Michael Henson on 26 March 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import datetime


def weekends(date1, date2):
    '''
    http://stackoverflow.com/questions/3615375/python-count-days-ignoring-weekends
    '''
    weekenddays = 0
    delta = datetime.timedelta(days=1)
    while date2 != date1:
        date2 -= delta
        if date2.isoweekday() not in (1, 2, 3, 4, 5):
            weekenddays += 1
    print('There are {} weekend days between {} and {}' .format(weekenddays, date1, date2))


def main():
    today = datetime.datetime(2016, 3, 16)
    enddate = datetime.datetime(2016, 12, 31)
    weekends(today, enddate)


if __name__ == '__main__':
    main()
