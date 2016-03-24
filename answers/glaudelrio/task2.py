#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 21:44:43 2016

@author: Glaucia Del-Rio
"""

import datetime


def weekend_days():
    """Counts the number of weekend days until the end of 2016"""
    last_day = datetime.date(2016, 12, 31)
    current_day = datetime.date.today()
    counter = 0
    weekend = [5, 6]
    while current_day <= last_day:
        if current_day.weekday() in weekend:
            counter += 1
        current_day += datetime.timedelta(days=1)
    return counter


def main():
    number_days = weekend_days()
    print("There are " + str(number_days) +
          """ weekend days until the end of 2016!""")

if __name__ == '__main__':
    main()
