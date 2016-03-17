#! usr/bin/env python
# encoding: utf-8

"""
Assignment 15
Task 2 Program: How many weekends are left?
Jessie Salter
16 March 2016
"""

import datetime


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
    today = datetime.date.today()
    end_date = datetime.date(2016, 12, 31)
    time_left = end_date - today
    # Adding one makes it inclusive if the start or end date is a weekend:
    days_left = time_left.days + 1
    alldays = []
    # This creates a list of the dates between start and end date (inclusive):
    for day in range(0, days_left):
        alldays = everyday(today, day, alldays)
    result = weekends(alldays)
    print('There are {} weekend days left in 2016.'.format(result))


if __name__ == '__main__':
    main()
