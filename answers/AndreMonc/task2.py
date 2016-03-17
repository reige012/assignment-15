# !/usr/bin/env python
# encoding: utf-8


"""
My weekend-counting program
Created by Andre Moncrieff on 16 March 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import datetime
import calendar


def days_left_2016():
    dt0 = datetime.date.today()
    dt1 = datetime.date(2016, 12, 31)
    difference = dt1 - dt0
    return difference


def num_weekend_days():
    dt0 = datetime.date.today()
    dt1 = datetime.date(2016, 12, 31)
    dtdelta = dt1-dt0
    weekend_days = 0
    for days in range(int(str(dtdelta)[:3])+1):
        if (calendar.day_name[dt0.weekday()] == "Saturday" or
            calendar.day_name[dt0.weekday()] == "Sunday"):
            weekend_days += 1
            dt0 += datetime.timedelta(days=1)
        else:
            dt0 += datetime.timedelta(days=1)
    return weekend_days


def main():
    nwd = num_weekend_days()
    print("\nThe number of weekend days between today and the" +
          " end of 2016 (inclusive end date): ", nwd, "\n")


if __name__ == '__main__':
    main()
