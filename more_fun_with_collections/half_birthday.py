"""
Program: half_birthday.py
Author: Paul Elsea
Last Modified: 06/24/2020

Program to average scores for a dictionary key chosen by the user.
"""

'''Imported datetime and dateutil modules'''
import datetime
from dateutil.relativedelta import relativedelta

'''Takes an input date and returns date 6 months later.
:date_in: Starting date input by program.
:date_out: Date 6 months after date_in
:returns: date_out'''
def half_birthday(date_in):
    date_out = date_in + relativedelta(months=+6)
    return date_out


if __name__ == '__main__':
    six_months_later = half_birthday(datetime.date(1900, 1, 1))
    print(six_months_later)