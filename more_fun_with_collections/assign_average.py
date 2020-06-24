"""
Program: assign_average.py
Author: Paul Elsea
Last Modified: 06/24/2020

Program to average scores from a dictionary populated by user input.
"""

'''This declares a dictionary, then prompts user for a group of scores to average. Results of averaged group
of scores is printed, or error message is displayed and user is prompted for new input.
:scores_dict: Dictionary of scores to be averaged
:input_scores: Number of scores prior to being validated as integer.
:num_scores: Input number of total scores to be asked for after validation.
:input_score: Each individual score to be validated and inserted into the dictionary.
:returns: Populated score dictionary'''

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

def get_input():
    user_choice = input('Please choose score set A, B, C, or D.\n')
    return user_choice

def get_test_scores():
    scores_dict = {}

    input_scores = input('Please enter number of scores:\n')
    while True:
        try:
            num_scores = int(input_scores)
            break
        except ValueError:
            input_scores = input('Please try again and use only numerals for number of scores:\n')
            continue


    for score in range(num_scores):
        while True:
            try:
                input_score = float(input('Please enter score #' + str(score+1) + ':\n'))
                if 0.00 > input_score or input_score > 100.00:
                    if input_score > 100.00:
                        print('Score is above maximum. Please enter score between 0 and 100')
                        continue
                    else:
                        print('Score is below minimum. Please enter score between 0 and 100')
                        continue

                scores_dict.update({'Score ' + str(score + 1): input_score})
                break

            except ValueError:
                print('Please enter scores using only numbers and one "."')
                continue

    return scores_dict

'''This takes an input dictionary, totals the scores within it, then averages them.
:input_dict: Dictionary of scores to be averaged
:score_total: Declared variable to contain totalled scores from dictionary.
:returns: String including average score of entries in input dictionary'''

def average_scores(input_dict, key_choice):
    score_total = 0.0
    for value in input_dict[key_choice]:
        score_total += value
    return str('Average score is: ' + str(score_total / len(input_dict[key_choice])))

if __name__ == '__main__':
    scores_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [0]}
    print(switch_average(scores_dict))