# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 15
Oscar Johnson 16 March 2016
"""

import argparse
import datetime


def get_args():
    parser = argparse.ArgumentParser(
            description="""calculate # of weekend days between two dates""")
    parser.add_argument('--start_date',
                        type=str,
                        required=True,
                        help="enter a start date in format: 2010,1,31",
                        )
    parser.add_argument('--end_date',
                        type=str,
                        required=True,
                        help="enter an end date in format: 2010,1,31",
                        )
    return parser.parse_args()


def weekend_days(args):
    """calculates the number of weekend days between user-specified dates"""
    counter = 0
    d = datetime.timedelta(days=1)
    while args.start_date <= args.end_date:
        # check if day is Sunday
        if args.start_date.weekday() is 5:
            counter += 1
        # check if day is Saturday
        elif args.start_date.weekday() is 6:
            counter += 1
        args.start_date += d
    return counter


def main():
    args = get_args()
    # convert input dates to datetime format
    args.start_date = datetime.datetime.strptime(args.start_date, '%Y,%m,%d')
    args.end_date = datetime.datetime.strptime(args.end_date, '%Y,%m,%d')
    result = weekend_days(args)
    print("the number of weekend days between your dates is: {}".format(result))

if __name__ == '__main__':
    main()
