#!/usr/bin/env python
# encoding: utf-8

"""
My  3rd program for Assignment 15

Created by Michael Henson on 26 March 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import datetime
import argparse


def askingforfiles():
    parser = argparse.ArgumentParser(
        description="Asking for start date and end day")
    parser.add_argument(
        "--start",
        required=True,
        help="Provide start date in Year Month Day format (example: 2016_03_16)",
        type=str
    )
    parser.add_argument(
        "--end",
        required=True,
        help="Provide end date in Year Month Day format (example: 2016_03_16)",
        type=str
    )
    return parser.parse_args()


def weekends(date1, date2):
    now = date1.replace("_", ", ")
    end = date2.replace("_", ", ")
    date1 = datetime.datetime.strptime(now, "%Y, %m, %d")
    date2 = datetime.datetime.strptime(end, "%Y, %m, %d")
    weekenddays = 0
    delta = datetime.timedelta(days=1)
    while date2 != date1:
        date2 -= delta
        if date2.isoweekday() not in (1, 2, 3, 4, 5):
            weekenddays += 1
    print('There are {} weekend days between {} and {}' .format(weekenddays, date1, date2))


def main():
    args = askingforfiles()
    weekends(args.start, args.end)


if __name__ == '__main__':
    main()
