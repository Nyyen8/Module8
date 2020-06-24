"""
Program: test_half_birthday.py
Author: Paul Elsea
Last Modified: 06/24/2020

Program to average scores for a dictionary key chosen by the user.
"""


import unittest
import datetime
from more_fun_with_collections import half_birthday as half

class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        test_date = datetime.datetime(1979, 1, 5)
        self.assertEqual(half.half_birthday(test_date), datetime.datetime(1979, 7, 5))


if __name__ == '__main__':
    unittest.main()
