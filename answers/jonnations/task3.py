#!/usr/bin/env python
# utf-8

"""
Assignment 15, Task 3
Jon Nations on 15 March 2016
Takes a start year, month, and day and a end year, month and day and tells you
the number of weekend days between them.
"""

import argparse
import datetime


def date_in():
    """takes numerical start Year, Month, Date and end Year, Month, Date.
        All 6 flags must be entered in the format  -sy 2016 -sm 03 -sd 15 -ey
         2016 -em 12 -ed 31"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-sy', '--syear', required=True, type=int,
                        help="give year of start date like 2016")
    parser.add_argument('-sm', '--smonth', required=True, type=int,
                        help="give month of start date like 03")
    parser.add_argument('-sd', '--sday', required=True, type=int,
                        help="give day of start date like 15")
    parser.add_argument('-ey', '--eyear', required=True, type=int,
                        help="give year of end date like 2016")
    parser.add_argument('-em', '--emonth', required=True, type=int,
                        help="give month of end date like 03")
    parser.add_argument('-ed', '--eday', required=True, type=int,
                        help="give day of end date like 15")
    return parser.parse_args()


def weekend(args, start, end):
    weekend_days = 0
    difference = (end - start).days
    for i in range(difference):
        current = start + datetime.timedelta(i)
        day = datetime.date.weekday(current)
        if day >= 5:
                weekend_days += 1
    print('\nThere are', weekend_days,
          'weekend days between', start, 'and', end, '\n')


def main():
    date_in()
    args = date_in()
    start = datetime.date(args.syear, args.smonth, args.sday)
    # start = datetime.date(args.start)
    end = datetime.date(args.eyear, args.emonth, args.eday)
    weekend(args, start, end)

if __name__ == '__main__':
    main()
