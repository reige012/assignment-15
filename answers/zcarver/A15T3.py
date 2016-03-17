#! /usr/bin/env python
# encoding UTF-8

'''
Assignment15Task3 biol7800
ZacCarver 03/17/2016
Takes the date inputs of user and computes the weekend days between.
'''

import argparse
import datetime


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start',
                        help='enter date in yyyy,mm,dd format')
    parser.add_argument('--end',
                        help='enter date in yyyy,mm,dd format')

    return parser.parse_args()


def weekend_days(start, end):
    #quite minimalist way of calculating the weekends. Derived from:
    #archugs.blogspot.com/2014/08/calculating-number-of-working-days.html
    return sum([1 for delt in xrange(1, (end - start).days+1)
                if (start + datetime.timedelta(delt)).weekday() > 5])


def main():
    arg = args()
    start = arg.start.split(',')
    end = arg.end.split(',')
    '''because datetime.date requires int, each element was first split on ','
    and then converted to an int. Presumably type=int could not be used in
    ars() is due to the ','??'''
    s = datetime.date(int(start[0]), int(start[1]), int(start[2]))
    e = datetime.date(int(end[0]), int(end[1]), int(end[2]))
    #s = datetime(start)
    #e = datetime(end)
    wd = weekend_days(s, e)
    print('{} days betweens dates given.'.format(wd))

if __name__ == '__main__':
    main()
