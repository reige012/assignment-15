#! usr/bin/env python
# encoding: utf-8

"""
Assignment 15
Task 3 Program: How many weekends are left (user input)
Jessie Salter
16 March 2016
"""

import argparse
import datetime


def parser():
    '''Takes user input'''
    parser = argparse.ArgumentParser(
        description='''Gets the paths of the input and output files.'''
    )
    parser.add_argument(
        "--startdate",
        required=True,
        help="Enter the start date: year month day",
        nargs='+',
        type=int
    )
    parser.add_argument(
        "--enddate",
        required=True,
        help="Enter the end date: year month day",
        nargs='+',
        type=int
    )
    return parser.parse_args()


def everyday(start, day, alldays):
    '''Adds each successive day to a list of all dates'''
    alldays.append(start + datetime.timedelta(days=day))
    return alldays


def weekends(dates):
    '''Creates a dictionary of dates and their weekday integer values,
    converts that dictionary into a list, creates a new list of weekend dates,
    prints the length of that list for total count of weekend days.'''
    # This creates a dictionary with date as key, integer day of week as value:
    weekday = dict()
    for day in dates:
        weekday[day] = datetime.date.weekday(day)
    weekday_list = []
    # Converts that dictionary into a list so it is accessible by value:
    for date, count in weekday.items():
        weekday_list.append([date, count])
    weekends = []
    # This creates a list of only weekend days:
    for item in weekday_list:
        if item[1] == 5:
            weekends.append(item)
        elif item[1] == 6:
            weekends.append(item)
    total_weekends = len(weekends)
    return total_weekends


def main():
    args = parser()
    start = datetime.date(
        year=args.startdate[0], month=args.startdate[1], day=args.startdate[2]
        )
    end = datetime.date(
        year=args.enddate[0], month=args.enddate[1], day=args.enddate[2]
        )
    time_left = end - start
    # Adding one makes it inclusive if the start or end date is a weekend:
    days_left = time_left.days + 1
    alldays = []
    # This creates a list of the dates between start and end date (inclusive):
    for day in range(0, days_left):
        alldays = everyday(start, day, alldays)
    result = weekends(alldays)
    if result == 0:
        print(
            'There are {} weekend days between {} and {}.'.format(
                result, start, end
                )
        )
    elif result == 1:
        print(
            'There is {} weekend day between {} and {}.'.format(
                result, start, end
                )
        )
    elif result > 1:
        print(
            'There are {} weekend days between {} and {}.'.format(
                result, start, end
                )
        )


if __name__ == '__main__':
    main()
