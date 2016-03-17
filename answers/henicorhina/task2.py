# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 15
Oscar Johnson 16 March 2016
"""

import datetime


def weekend_days(today):
    """calculates the number of weekend days left this year"""
    end_of_year = today.replace(month=12, day=31)
    counter = 0
    # weekend = (5,6)
    d = datetime.timedelta(days=1)
    while today <= end_of_year:
        # check if day is Sunday
        if today.weekday() is 5:
            counter += 1
        # check if day is Saturday
        elif today.weekday() is 6:
            counter += 1
        today += d
    return counter


def main():
    today = datetime.date(2016, 3, 16)
    result = weekend_days(today)
    print("the number of weekend days left this year is: {}".format(result))

if __name__ == '__main__':
    main()
