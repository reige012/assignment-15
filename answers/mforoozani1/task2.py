#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task2 to determines, from now until the end of 2016,
how many weekend days there are
"""
import datetime
import numpy as np


def weekend_day():
    """
use datetime.datetime to get the start and end time. use np.busday_count to
calculate busniess day and then weekend days
    """
    today = datetime.date(2016, 3, 16)
    end_2016 = datetime.date(2016, 12, 31)
    end_day_included = datetime.date(2017, 1, 1)
    total = end_2016 - today
    A = total.days
    # print(A)
    businessdays = np.busday_count(today, end_day_included)
    # print(businessdays)
    weekend_count = A - businessdays
    return weekend_count


def main():
    result = weekend_day()
    print(result)


if __name__ == '__main__':
    main()
