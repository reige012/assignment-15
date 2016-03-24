#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task2 to determines, from now until the end of 2016,
how many weekend days there are
"""
import datetime
import numpy as np
import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description=""" take the start and end times on the command line"""
        )

    parser.add_argument(
        "--y1",
        required=True,
        # nargs='+',
        type=int,
        help="""input the start date, year"""
        )
    parser.add_argument(
        "--m1",
        required=True,
        # nargs='+',
        type=int,
        help="""input the start date,month """
        )
    parser.add_argument(
        "--d1",
        required=True,
        # nargs='+',
        type=int,
        help="""input the start date, day"""
        )
    parser.add_argument(
        "--y2",
        required=True,
        # nargs='+',
        type=int,
        help="""input the end date, year"""
        )
    parser.add_argument(
        "--m2",
        required=True,
        # nargs='+',
        type=int,
        help="""input the end date, month"""
        )
    parser.add_argument(
        "--d2",
        required=True,
        # nargs='+',
        type=int,
        help="""input the end date, day"""
        )
    parser.add_argument(
        "--y3",
        required=True,
        # nargs='+',
        type=int,
        help=""" input the day after the end date  , year"""
        )
    parser.add_argument(
       "--m3",
       required=True,
       # nargs='+',
       type=int,
       help=""" input the day after the end date  ,month """
       )
    parser.add_argument(
       "--d3",
       required=True,
       # nargs='+',
       type=int,
       help=""" input the day after the end date  , day"""
       )
    args = parser.parse_args()
    return args


def main():
    args = get_parser()
    today = datetime.date(args.y1, args.m1, args.d1)
    end_2016 = datetime.date(args.y2, args.m2, args.d2)
    end_day_included = datetime.date(args.y3, args.m3, args.d3)
    total = end_2016 - today
    A = total.days
    # print(A)
    businessdays = np.busday_count(today, end_day_included)
    # print(businessdays)
    weekend_count = A - businessdays
    print(weekend_count)


if __name__ == '__main__':
    main()
