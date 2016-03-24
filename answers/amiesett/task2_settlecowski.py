#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 15 Task 2

Amie Settlecowski
18 Mar. 2016

Output the count of weekend days between today and the last day of the year.
"""


import datetime


def count_weekends(start, end):
    date = start
    count = 0
    while date != end:
        if date.weekday() == 5 or date.weekday() == 6:
            count += 1
        date += datetime.timedelta(days=1)
    return count


def main():
    today = datetime.date.today()
    end_of_year = datetime.date(2016, 12, 31)
    nweekends = count_weekends(today, end_of_year)
    print('There are {} weekend days between {} and {}.'.format(nweekends,
                                                                today,
                                                                end_of_year))
if __name__ == '__main__':
    main()
