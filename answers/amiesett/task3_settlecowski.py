#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 15 Task 3

Amie Settlecowski
18 Mar. 2016

Output number of weekend days between user specified start and end dates.
To use:
python ../task3_settlecowski.py --start YYYY-MM-DD --end YYYY-MM-DD
"""

import argparse
import datetime


def get_args(parserr):
    '''
    Requires --start, --end flags to specify start and end dates respectively
    '''
    parserr.add_argument("--start",
                            required=True,
                            help="Start date in the format YYYY-MM-DD",
                            type=str)
    parserr.add_argument("--end",
                            required=True,
                            help="End date in the format YYYY-MM-DD",
                            type=str)


def construct_date(date_arg):
    '''Create date object from arguments input by user.'''
    date_as_list = date_arg.split('-')
    date = datetime.date(int(date_as_list[0]),
                        int(date_as_list[1]),
                        int(date_as_list[2]))
    #print('testing construct date: ', date)
    return date


def count_weekends(start, end):
    date = start
    count = 0
    while date != end:
        if date.weekday() == 5 or date.weekday() == 6:
            count += 1
        date += datetime.timedelta(days=1)
    return count


def main():
    # creater Parser object with arguments for start and end dates
    date_parser = argparse.ArgumentParser()
    get_args(date_parser)
    date_args = date_parser.parse_args()
    # construct date objects from user inputs
    start_date = construct_date(date_args.start)
    end_date = construct_date(date_args.end)

    nweekends = count_weekends(start_date, end_date)
    print('There are {} weekend days between {} and {}.'.format(nweekends,
                                                                start_date,
                                                                end_date))
if __name__ == '__main__':
    main()
