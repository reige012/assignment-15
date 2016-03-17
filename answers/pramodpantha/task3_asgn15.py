#!/usr/bin/env python
# utf-8


"""
program for task3 of assignment 15.
This program gives total number of weekend days from the two specifed" +
" point of time. This program does not take any consideration for" +
" government holidays, it just counts total weekend days" +
" (saturday and sunday)
Created by Pramod Pantha on 16 March, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


from datetime import date
import argparse


def weekenddays_counter(start_date, end_date):
    start_week_days = min(start_date.weekday(), 4) + 1
    end_week_days = min(end_date.weekday(), 4) + 1
    no_of_weeks = end_date.isocalendar()[1] - start_date.isocalendar()[1]
    working_days = (5 * no_of_weeks) + end_week_days - start_week_days
    if start_date.weekday() < 5:
        working_days += 1
    # reference from: http://archugs.blogspot.com/2014/08/calculating-" +
    # number-of working-days.html
    date_delta = (end_date - start_date).days
    weekend = date_delta - working_days
    return weekend


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_date", help="Enter start date as:" +
                        " yyyy,mm,dd")
    parser.add_argument("--end_date", help="Enter end date as:" +
                        " yyyy,mm,dd")
    args = parser.parse_args()
    # can accept any two point of time and give total number of weekend days" +
    # " if dates are in the specified format above
    start1 = args.start_date.split(',')
    end1 = args.end_date.split(',')
    start = date(int(start1[0]), int(start1[1]), int(start1[2]))
    end = date(int(end1[0]), int(end1[1]), int(end1[2]))
    x = weekenddays_counter(start, end)
    print("Total number of weekend days: ", x)
    # prints look like: Total number of weekend days: (number here after :)

if __name__ == '__main__':
    main()
