"""
Program: assign_average.py
Author: Paul Elsea
Last Modified: 06/24/2020

Program to average scores for a dictionary key chosen by the user.
"""

'''This takes in a dictionary, prompts user for a group of scores to average. Results of averaged group
of scores is returned, or an error message if user inputs invalid data.
:input_dict: The dictionary that the user is choosing which key to work with
:choice: The key the user will select to work with
:returns: Averaged scores of chosen dictionary key or an error message'''

def switch_average(input_dict):
    while True:
        choice = get_input()

        if choice == 'A' or choice =='a':
            return average_scores(input_dict, 'A')
        if choice == 'B' or choice == 'b':
            return average_scores(input_dict, 'B')
        if choice == 'C' or choice =='c':
            return average_scores(input_dict, 'C')
        if choice == 'D' or choice =='d':
            return average_scores(input_dict, 'D')
        else:
            return "I'm sorry, I didn't recognize that. Please choose either A, B, C, or D.\n"

'''This prompts user for an letter choice which is returned.
:user_choice: The key chosen by the user.
:returns: Char or string entered by the user'''

def get_input():
    user_choice = input('Please choose score set A, B, C, or D.\n')
    return user_choice

'''This takes an input dictionary and key, totals the scores associated with the key, then averages them.
:input_dict: Dictionary of scores to be averaged
:key_choice: The key chosen by the user for which scores they wanted averaged.
:score_total: Declared variable to contain totalled scores from dictionary.
:returns: String including average score of entries for input dictionary key'''

def average_scores(input_dict, key_choice):
    score_total = 0.0
    for value in input_dict[key_choice]:
        score_total += value
    return str('Average score is: ' + str(score_total / len(input_dict[key_choice])))

if __name__ == '__main__':
    scores_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [0]}
    print(switch_average(scores_dict))