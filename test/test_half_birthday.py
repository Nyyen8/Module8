"""
Program: test_half_birthday.py
Author: Paul Elsea
Last Modified: 06/24/2020

Program to test half_birthday().
"""


import unittest
import datetime
from more_fun_with_collections import half_birthday as half

'''Test to ensure half_birthday produces correct dates'''
class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        test_date_1 = datetime.datetime(1979, 7, 5)
        test_date_2 = datetime.datetime(1984, 1, 10)
        test_date_3 = datetime.datetime(1998, 12, 31)
        self.assertEqual(half.half_birthday(test_date_1), datetime.datetime(1980, 1, 5))
        self.assertEqual(half.half_birthday(test_date_2), datetime.datetime(1984, 7, 10))
        self.assertEqual(half.half_birthday(test_date_3), datetime.datetime(1999, 6, 30))


if __name__ == '__main__':
    unittest.main()
