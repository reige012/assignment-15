#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:39:34 2016

@author: Glaucia
"""

import argparse

import datetime


def arguments():
    """Parsing arguments to have input file"""
    parser = argparse.ArgumentParser(description="""my argument parser""")
    parser.add_argument('final_date', help="""the final date YYYY-MM-DD""")
    parser.add_argument('start_date', help="""the start date YYYY-MM-DD""")
    args = parser.parse_args()
    final_date = args.final_date
    start_date = args.start_date
    return final_date, start_date


def weekend_days(final_date, start_date):
    """Counts the number of weekend days between starting and final dates
    given by the user in the format YYYY-MM-DD"""
    final_date = datetime.datetime.strptime(final_date, "%Y-%m-%d")
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    counter = 0
    weekend = [5, 6]
    while start_date <= final_date:
        if start_date.weekday() in weekend:
            counter += 1
        start_date += datetime.timedelta(days=1)
    return counter


def main():
    final = arguments()[0]
    start = arguments()[1]
    number_days = weekend_days(final, start)
    print("\rThere are " + str(number_days) +
          """ weekend days between your starting and final date!""")

if __name__ == '__main__':
    main()
