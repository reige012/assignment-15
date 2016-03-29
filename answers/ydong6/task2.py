#!/usr/bin/env python
# encoding: utf-8
'''
Created on Mar 17, 2016
Task 2
When you're working with field data, you often need to manipulate dates. Using
the datetime module, write a program that determines, from now until the end of
2016, how many weekend days there are. You don't need to take any input from the
user, and you can output the answer to the screen (it would be helpful if you
could format this reasonably to explain what is being output). Your program
should contain a main loop and an ifmain statement, and it should be formatted
correctly. You should run a linter against your code to make sure you have
formatted it according to PEP8.
@author: York
'''
import datetime


def amount_weekends(d1 , d2):
    dura = d1
    counter = 0
    while d2 != d1:
        d2 -= datetime.timedelta(1)  #-1 if d2 is larger than d1
        if dura.weekday() == 5:  #or use isoweekday()
            counter += 1
        elif dura.weekday() == 6:  #Return the day of the week as an integer, where Monday is 0 and Sunday is 6
            counter += 1
        dura += datetime.timedelta(1)  #A timedelta object represents the difference between two dates or times.
    return counter


def main():
    d1 = datetime.date.today()
    d2 = datetime.date(2017, 1, 1)
    weekends = amount_weekends(d1, d2)
    print("The total weekends between {} and {} is {}".format(d1, d2 , weekends))


if __name__ == '__main__':
    main()
