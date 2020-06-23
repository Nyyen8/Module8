"""
Program: set_membership.py
Author: Paul Elsea
Last Modified: 06/23/2020

Program to .
"""

'''Function to determine if element is included in an input set.
:input_set: Set to be searched.
:search_variable: What is being searched for in the input set.
:returns: True/False depending on if variable is in set.'''
def in_set(input_set, search_variable):
    if search_variable in input_set:
        return True
    else:
        return False

if __name__ == '__main__':
    a_set = set('aslkfdjaef')

    print(in_set(a_set, 's'))
    print(in_set(a_set, 3))
