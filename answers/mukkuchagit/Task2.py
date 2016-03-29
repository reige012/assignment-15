#!/usr/bin/env python
# encoding: utf-8
"""
assignment 15.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import datetime


def no_of_weekend_days():
    today = datetime.date.today()
    print("Today : ", today)
    endDay = datetime.date(today.year, 12, 31)
    print("End of Year : ", endDay)
    daysDiff = (endDay - today).days
    print("Number of days between today and end of this year : ", daysDiff)
    numberOfWeekends = (daysDiff*2)//7
    return numberOfWeekends


def main():
    Total_weekend_days = no_of_weekend_days()
    print("Weekends count : ", Total_weekend_days)


if __name__ == '__main__':
    main()
