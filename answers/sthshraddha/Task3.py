#!/usr/bin/env python

"""
Assignment15_Task3:
Modify Task2 using argparse to accept user start date and end date.

Is not working.

Credit urls:
Date accessed: 03/16/2016
Date accessed: 03/16/2016

Created by Shraddha Shrestha on March 16, 2016.
"""

import datetime
import argparse


def get_parser():
    """Get start and end date from user"""
    parser = argparse.ArgumentParser(
            description="""Getting start date""")
    parser.add_argument(
            "--startdate",
            required=True,
            type=valid_date,
            help="""startdate format- YYYY-MM-DD"""
            )
    parser.add_argument(
            "--enddate",
            required=True,
            type=valid_date,
            help="""enddate format- YYYY-MM-DD"""
            )
    return parser.parse_args()


def valid_date(args):
    try:
        return datetime.strptime(args, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date:'{0}'.".format(args)
        raise argparse.ArgumentTypeError(msg)


def getting_total_weekends(args):
    start_date = datetime.datetime(args.startdate)
    end_date = datetime.datetime(args.enddate)
    days_remaining = abs(start_date - end_date)
    remaining_weeks = (days_remaining.days)/7
    # using .days gives JUST the integer
    number_of_weekends = (remaining_weeks)*2
    # multiplying the number of weeks by 2 gives number of weekends
    return number_of_weekends


def main():
    args = get_parser()
    valid_date = valid_date(args)
    args.startdate = datetime.datetime.strptime(args.startdate, '%Y-%m-%d')
    args.enddate = datetime.datetime.strptime(args.enddate, '%Y,%m,%d')
    result = getting_total_weekends(args)
    #print("the number of weekend days between your dates is: {}".format(result))
    print("{0:0.0f}".format(result))


if __name__ == '__main__':
    main()
