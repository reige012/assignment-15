#! /usr/bin/env python
# encoding UTF-8

'''
Assignment15Task2 biol7800
ZacCarver 03/17/2016
Takes user input and calculates weekend days between now and the end of the yr.
'''

from datetime import date, timedelta


def weekends(now, then):
    #quite minimalist way of calculating the weekends. Derived from:
    #archugs.blogspot.com/2014/08/calculating-number-of-working-days.html
    return sum([1 for delt in xrange(1, (then - now).days+1)
                if (now + timedelta(delt)).weekday() > 5])


def main():
    now = date(2016, 3, 17)
    then = date(2016, 12, 31)
    #print(weekends(now, then))
    print('total weekends from {} to {} is {}'.format(now, then, weekends(now, then)))

if __name__ == '__main__':
    main()
