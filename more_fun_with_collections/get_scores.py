"""
Program: get_scores.py
Author: Paul Elsea
Last Modified: 06/24/2020

Program to average scores from a dictionary populated by user input.
"""

'''This declares a dictionary, then prompts for total number of scores. Using this it prompts user
for each score in turn and adds them to the dictionary. Resulting filled dictionary is returned.
:scores_dict: Dictionary to be populated by user input
:input_scores: Number of scores prior to being validated as integer.
:num_scores: Input number of total scores to be asked for after validation.
:input_score: Each individual score to be validated and inserted into the dictionary.
:returns: Populated score dictionary'''

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

def average_scores(input_dict):
    score_total = 0.0
    for score, value in input_dict.items():
        score_total += value
    return str('Average score is: ' + str(score_total / len(input_dict)))

if __name__ == '__main__':
    print(average_scores(get_test_scores()))