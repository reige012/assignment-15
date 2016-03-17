#!/usr/bin/env python
# utf-8


"""
program for task2 of assignment 15.
This program gives total number of weekend days from the two specifed" +
" point of time. This program does not take any consideration for" +
" government holidays, it just counts total weekend days" +
" (saturday and sunday)
Created by Pramod Pantha on 16 March, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


from datetime import date


def weekenddays_counter():
    start_date = date(2016, 3, 16)
    end_date = date(2016, 12, 31)
    # it calculate number of days in starting and ending week
    start_week_days = min(start_date.weekday(), 4) + 1
    end_week_days = min(end_date.weekday(), 4) + 1
    # it calculate number of weeks between the dates I have given
    no_of_weeks = end_date.isocalendar()[1] - start_date.isocalendar()[1]
    working_days = (5 * no_of_weeks) + end_week_days - start_week_days
    # it includes the starting day if it is weekday
    if start_date.weekday() < 5:
        working_days += 1
    # reference from: http://archugs.blogspot.com/2014/08/calculating-" +
    # number-of working-days.html
    date_delta = (end_date - start_date).days
    # gives total number of days from start/today to end of this year
    weekend = date_delta - working_days
    # gives total number of weekends between two point of time
    return weekend


def main():
    x = weekenddays_counter()
    print("Total number of weekend days: ", x)
    # prints looks: Total number of weekend days: (number here after :)

if __name__ == '__main__':
    main()
