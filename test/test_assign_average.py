"""
Program: assign_average.py
Author: Paul Elsea
Last Modified: 06/24/2020

Program to average scores from a dictionary populated by user input.
"""

import unittest
from unittest.mock import patch
from more_fun_with_collections import assign_average as ave

class AverageTestCases(unittest.TestCase):
    @patch('more_fun_with_collections.assign_average.get_input', return_value='A')
    def test_Aa_input(self, input):
        test_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': 0}
        self.assertEqual(ave.switch_average(), 'Average score is: 2.0')


if __name__ == '__main__':
    unittest.main()
