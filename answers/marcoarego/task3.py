# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Marco
# @Date:   2016-03-16 17:34:18
# @Last Modified by:   Marco
# @Last Modified time: 2016-03-16 23:08:52


import argparse
import datetime


def my_parser():
    '''
    Function to parse arguments from the terminal
    '''
    parser = argparse.ArgumentParser(description="""This is the argument
    parser. This code calculates the number of weekend days we will have
     between present date and a future date. The input data should be
     equivalent to the future date.\n\nCAUTION! This code uses a recursive
     function. It works for the purpose of this exercise, but don't input a
     large range of time.\n Please enter 3 integer arguments:
    \nYEAR, MONTH and DAY. They must be in this exact same order!!!
    """)
    parser.add_argument('year', type=int, help='enter the year')
    parser.add_argument('month', type=int, help='enter the month')
    parser.add_argument('day', type=int, help='enter the day')
    args = parser.parse_args()
    y = args.year
    m = args.month
    d = args.day
    return y, m, d


def weekdays_list(today=datetime.date.today(),
                  future_day=datetime.date(datetime.date.today().year,
                  datetime.date.today().month, 31),
                  week_list=[]):
    '''
    CAUTION! RECURSIVE FUNCTION.
    Function that gets a initial date and a future date, returning a list
    of weekdays. The length of this list corresponds to the difference in
    days between the two dates.
    '''
    if today <= future_day:
        week_list.append(today.weekday())
        return weekdays_list(today+datetime.timedelta(days=1), future_day)
    else:
        pass
    return week_list


def main():
    y, m, d = my_parser()
    my_list = weekdays_list(today=datetime.date.today(),
                            future_day=datetime.date(y, m, d))
    saturdays = my_list.count(5)
    sundays = my_list.count(6)
    weekdays = saturdays + sundays
    print('\nWe have {} weekend days left until {}/{}/{}. Or '
          '{} Saturdays and {} Sundays'.format(weekdays, y, m, d, saturdays,
                                               sundays))


if __name__ == '__main__':
    main()
