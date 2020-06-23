"""
Program: dict_membership.py
Author: Paul Elsea
Last Modified: 06/23/2020

Program to see if an element is included in a dict.
"""

'''Function to determine if element is included in an input dictionary.
:input_set: Dictionary to be searched.
:search_variable: What is being searched for in the input dictionary.
:returns: True/False depending on if variable is in dictionary.'''
def in_dict(input_dict, search_variable):
    if search_variable in input_dict:
        return True
    else:
        return False

if __name__ == '__main__':
    a_dict = {'A': 1, 'B': 2, 'C': 3}

    print(in_dict(a_dict, 'A'))
    print(in_dict(a_dict, 3))
