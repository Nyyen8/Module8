"""
Program: test_set_membership.py
Author: Paul Elsea
Last Modified: 06/23/2020

Program to test functions of set_membership.py.
"""

import unittest
from more_fun_with_collections import set_membership as set


class SetTestCases(unittest.TestCase):
    '''Test to make sure in_set() produced True return with variable found in provided set.'''
    def test_in_set_true(self):
        test_set = {1,2,3,4,5,6,7,8,9}
        self.assertTrue(set.in_set(test_set, 4))

    '''Test to make sure in_set() produced False return with variable not found in provided set.'''
    def test_in_set_false(self):
        test_set = {1,2,3,4,5,6,7,8,9}
        self.assertFalse(set.in_set(test_set, 'a'))


if __name__ == '__main__':
    unittest.main()
