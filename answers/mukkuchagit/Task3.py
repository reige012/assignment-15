#!/usr/bin/env python
# encoding: utf-8
"""
assignment 15.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import argparse
import datetime


def start_and_end_date(end_date, start_date):
    daysDiff = (end_date - start_date).days
    numberOfWeekends = (daysDiff*2)//7
    return daysDiff, numberOfWeekends


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("start_date", help="Enter start date as: mm-dd-yyyy")
    parse.add_argument("end_date", help="Enter end date as: mm-dd-yyyy")
    days = parse.parse_args()
    s_date = days.start_date.split('-')
    e_date = days.end_date.split('-')

    start_date = datetime.date(int(s_date[2]), int(s_date[0]), int(s_date[1]))
    end_date = datetime.date(int(e_date[2]), int(e_date[0]), int(e_date[1]))
    result = start_and_end_date(end_date, start_date)
    print("Today : ", start_date)
    print("End of Year : ", end_date)
    print("Number of days between today and end of this year : ", result[0])
    print("Weekends count : ", result[1])


if __name__ == '__main__':
    main()
