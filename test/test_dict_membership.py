"""
Program: test_dict_membership.py
Author: Paul Elsea
Last Modified: 06/23/2020

Program to test functions of dict_membership.py.
"""

import unittest
from more_fun_with_collections import dict_membership as dict


class DictTestCases(unittest.TestCase):
    '''Test to make sure in_dict() produced True return with variable found in provided dict'''
    def test_in_dict_true(self):
        test_dict = {'A': 1, 'B': 2, 'C': 3}
        self.assertTrue(dict.in_dict(test_dict, 'A'))

    '''Test to make sure in_dict() produced False return with variable not found in provided set.'''
    def test_in_dict_false(self):
        test_dict = {'A': 1, 'B': 2, 'C': 3}
        self.assertFalse(dict.in_dict(test_dict, 3))


if __name__ == '__main__':
    unittest.main()
