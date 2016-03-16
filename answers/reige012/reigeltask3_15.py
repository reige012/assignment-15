#!/usr/bin/env python
# encoding: utf-8

"""
This function determines the number of weekend days between two dates as input
by the user on the command line. The start date must be the earlier of the two
dates. Six arguments are requested on the command
line:
--syear: the starting date year. Format = yyyy
--smonth: the starting month. Format = mm
--sday: the starting day. Format = dd
--eyear: the ending date year. Format = yyy
--emonth: the ending date month. Format = mm
--eday: the ending date day. Format = dd
If you fail to input each of these flags the program will not function.

Edited by Alicia Reigel. 15 March 2016.
Copyright Alicia Reigel. Louisiana State University. 15 March 2016. All
rights reserved.

"""


import datetime
import argparse


def parser_dates():
    """Collects the start and end dates for the calculation"""
    parser = argparse.ArgumentParser(
        description="""Input the start and end dates for the calculation"""
        )
    parser.add_argument(
            '--syear',
            required=True,
            type=int,
            help='''Enter the start year in the format yyyy'''
        )
    parser.add_argument(
            '--smonth',
            required=True,
            type=int,
            help="Enter the start month in the format mm"
        )
    parser.add_argument(
            '--sday',
            required=True,
            type=int,
            help="Enter the start day in the format dd."
        )
    parser.add_argument(
            '--eyear',
            required=True,
            type=int,
            help="Enter the end year in the format yyyy"
        )
    parser.add_argument(
            '--emonth',
            required=True,
            type=int,
            help="Enter the end month in the format mm"
        )
    parser.add_argument(
            '--eday',
            required=True,
            type=int,
            help="Enter the end day in the format dd"
        )
    return parser.parse_args()


def figure_out_weekends(d1, d2):
    count_weekend_days = 0
    while d2 != d1:
        d2 -= datetime.timedelta(days=1)
        # while date2 is larger than date 1 then subtract a day
        if d2.isoweekday() not in range(1, 6):
            count_weekend_days += 1
        # if that day is not a weekday (1,6) then add it to the count
        # weekends are actually 6 & 7, but range requires me to add the six to get 1-5 inclusive
    return count_weekend_days


def main():
    args = parser_dates()
    date1 = datetime.date(args.syear, args.smonth, args.sday)
    date2 = datetime.date(args.eyear, args.emonth, args.eday)
    count_of_weekend_days = figure_out_weekends(date1, date2)
    date1_pretty = datetime.date.isoformat(date1)
    date2_pretty = datetime.date.isoformat(date2)
    print("There are {} weekend days between {} and {}.".format(count_of_weekend_days, date1_pretty, date2_pretty))


if __name__ == '__main__':
    main()
