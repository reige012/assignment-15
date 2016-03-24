# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Marco
# @Date:   2016-03-15 21:58:04
# @Last Modified by:   Marco
# @Last Modified time: 2016-03-16 22:30:41

import datetime


def weekdays_list(today, future_day, week_list=[]):
    '''
    CAUTION! RECURSIVE FUNCTION.
    Function that gets a initial date and a future date, returning a list
    of weekdays. The length of this list corresponds to the difference in
    days between the two dates.
    '''
    if today <= future_day:
        week_list.append(today.weekday())
        return weekdays_list(today+datetime.timedelta(days=1), future_day)
    else: # today == future_day:
        # week_list.append(today.weekday())
        pass
    return week_list


def main():
    t_initial = datetime.date.today()
    t_final = datetime.date(2016, 12, 31)
    my_list = weekdays_list(t_initial, t_final)
    saturdays = my_list.count(5)
    sundays = my_list.count(6)
    weekdays = saturdays + sundays
    print('\nWe have {} weekend days left until the end of 2016. Or '
          '{} Saturdays and {} Sundays'.format(weekdays, saturdays, sundays))


if __name__ == '__main__':
    main()
