#!/usr/bin/env python
# utf-8

"""
Assignment 15, Task 2
Jon Nations on 15 March 2016
This program tells you how many weekend days there are between today and the end of 2016
"""

import datetime


def weekend(today, end):
    weekend_days = 0
    difference = (end - today).days
    for i in range(difference):
        current = today + datetime.timedelta(i)
        day = datetime.date.weekday(current)
        if day >= 5:
                weekend_days += 1
    print('\nThere are', weekend_days,
          'weekend days from today until 2016-12-31\n')


def main():
    today = datetime.date.today()
    end = datetime.date(2016, 12, 31)
    weekend(today, end)

if __name__ == '__main__':
    main()
