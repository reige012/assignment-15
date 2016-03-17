# !/usr/bin/env python
# encoding: utf-8


"""
My weekend-counting program
Created by Andre Moncrieff on 17 March 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import datetime
import calendar
import argparse
import re


def parser():
    """
    Create argument input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_date",
                        nargs="+",
                        required=True,
                        help="Use following date format: month day year" +
                             " (for example, 12 31 2016)",
                        type=int)
    parser.add_argument("--end_date",
                        nargs="+",
                        required=True,
                        help="Use following date format: month day year" +
                             " (for example, 12 31 2016)",
                        type=int)
    args = parser.parse_args()
    return args


def days_left_2016():
    dt0 = datetime.date.today()
    dt1 = datetime.date(2016, 12, 31)
    difference = dt1 - dt0
    return difference


def num_weekend_days(start_date, end_date):
    dt0 = datetime.date(start_date[2], start_date[0], start_date[1])
    dt1 = datetime.date(end_date[2], end_date[0], end_date[1])
    dtdelta = dt1-dt0
    weekend_days = 0
    for days in range(int(re.findall(r"(\w+)\s.+", str(dtdelta))[0])+1):
        if (calendar.day_name[dt0.weekday()] == "Saturday" or
            calendar.day_name[dt0.weekday()] == "Sunday"):
            weekend_days += 1
            dt0 += datetime.timedelta(days=1)
        else:
            dt0 += datetime.timedelta(days=1)
    return weekend_days


def main():
    args = parser()
    nwd = num_weekend_days(args.start_date, args.end_date)
    print("\nThe number of weekend days between start date and end date" +
          " (inclusive): ", nwd, "\n")


if __name__ == '__main__':
    main()
