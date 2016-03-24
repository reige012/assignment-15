#!/usr/bin/env python

"""
Assignment15_Task3:
Finally got Task3 to work after playing around with and logically thinking \
about argparse :)

Credit urls:
http://stackoverflow.com/questions/12462074/python-argparse-create-timedelta-\
object-from-argument
Date accessed: 03/16/2016

http://stackoverflow.com/questions/25470844/specify-format-for-input-arguments-\
argparse-python
Date accessed: 03/16/2016

Created by Shraddha Shrestha on March 17, 2016.
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
            type=str,
            help="""startdate format- 2016-3-16"""
            )
    parser.add_argument(
            "--enddate",
            required=True,
            type=str,
            help="""enddate format- 2016-4-2"""
            )
    return parser.parse_args()


def getting_total_weekends(startdate, enddate):
    start_date = startdate
    end_date = enddate
    days_remaining = abs(start_date - end_date)
    remaining_weeks = (days_remaining.days)/7
    # using .days gives JUST the integer
    number_of_weekends = (remaining_weeks)*2
    # multiplying the number of weeks by 2 gives number of weekends
    return number_of_weekends


def main():
    args = get_parser()
    startdate = datetime.datetime.strptime(args.startdate, '%Y-%m-%d')
    enddate = datetime.datetime.strptime(args.enddate, '%Y-%m-%d')
    result = getting_total_weekends(startdate, enddate)
    print("{0:0.0f}".format(result))


if __name__ == '__main__':
    main()
