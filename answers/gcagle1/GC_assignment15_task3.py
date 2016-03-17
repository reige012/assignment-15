#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
14 March 2016
Assignment 15 Task 3

A program taking start and end times on the command line, and calculating the
number of weekends between them.

valid date code from http://stackoverflow.com/a/25470943 by jonrsharpe

'''

import argparse
import datetime
import time
import pdb

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', "--fromdate",
        required=True,
        help="The Start Date - format YYYY,MM,DD"
    )

    parser.add_argument(
        '-t', "--todate",
        required=True,
        help="The End Date - format YYYY,MM,DD"
    )
    return parser.parse_args()

'''
coudn't get this part to work but I like this approach:
def valid_date(fromdate):
    try:
        return time.strptime(fromdate, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(fromdate)
        raise argparse.ArgumentTypeError(msg)
'''


def weekend_finder2(fromdate, todate):
    daygenerator = (fromdate + datetime.timedelta(x + 1)
                    for x in range((todate - fromdate).days))
    print(sum(day.weekday() > 5 for day in daygenerator))


def main():
    args = get_args()
    todate1 = args.todate.split(',')
    todate = datetime.date(int(todate1[0]),int(todate1[1]),int(todate1[2]))
    fromdate1 = args.fromdate.split(',')
    fromdate = datetime.date(int(fromdate1[0]),int(fromdate1[1]),int(fromdate1[2]))
    weekend_finder2(fromdate, todate)


if __name__ == '__main__':
    main()
