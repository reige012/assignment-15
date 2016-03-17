#!/usr/bin/env python

"""
Assignment15_Task2:
Using the datetime module, write a program that determines, from now until the \
end of 2016, how many weekend days there are.

Credit urls:
http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
Date accessed: 03/16/2016
https://docs.python.org/2/library/datetime.html
Date accessed: 03/16/2016
Dr. Brant's lecture 14 slides
Date accessed: 03/16/2016

Created by Shraddha Shrestha on March 16, 2016.
"""

import datetime


def getting_total_weekends():
    start_date = datetime.datetime(2016, 3, 16)
    end_date = datetime.datetime(2016, 12, 31)
    days_remaining = abs(start_date - end_date)
    remaining_weeks = (days_remaining.days)/7
    # using .days gives JUST the integer
    number_of_weekends = (remaining_weeks)*2
    # multiplying the number of weeks by 2 gives number of weekends
    return number_of_weekends


def main():
    weekends_start_end = getting_total_weekends()
    print("\nThe number of weekends from today until end of year is:")
    # 0.0f means no decimal place after the integer so rounds up decimal places
    # to 1.
    print("{0:0.0f}".format(weekends_start_end))


if __name__ == '__main__':
    main()
