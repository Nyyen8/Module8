"""
Program: test_assign_average.py
Author: Paul Elsea
Last Modified: 06/24/2020

Program to test switch_average function from assign_average.py.
"""

import unittest
from unittest.mock import patch
from more_fun_with_collections import assign_average as ave

class AverageTestCases(unittest.TestCase):

    '''Test to verify correct return for "A" input'''
    @patch('more_fun_with_collections.assign_average.get_input', return_value='A')
    def test_Aa_input(self, input):
        test_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': 0}
        self.assertEqual(ave.switch_average(test_dict), 'Average score is: 2.0')

    '''Test to verify correct return for "B" input'''
    @patch('more_fun_with_collections.assign_average.get_input', return_value='B')
    def test_Bb_input(self, input):
        test_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': 0}
        self.assertEqual(ave.switch_average(test_dict), 'Average score is: 5.0')

    '''Test to verify correct return for "C" input'''
    @patch('more_fun_with_collections.assign_average.get_input', return_value='C')
    def test_Cc_input(self, input):
        test_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': 0}
        self.assertEqual(ave.switch_average(test_dict), 'Average score is: 8.0')

    '''Test to verify correct return for "D" input'''
    @patch('more_fun_with_collections.assign_average.get_input', return_value='D')
    def test_Dd_input(self, input):
        test_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [0]}
        self.assertEqual(ave.switch_average(test_dict), 'Average score is: 0.0')

    '''Test to verify correct return for bad input'''
    @patch('more_fun_with_collections.assign_average.get_input', return_value='x')
    def test_bad_input(self, input):
        test_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [0]}
        self.assertEqual(ave.switch_average(test_dict), "I'm sorry, I didn't recognize that. Please choose either A, B, C, or D.\n")


if __name__ == '__main__':
    unittest.main()
