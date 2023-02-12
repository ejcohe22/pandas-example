'''
classification_library.py
2/11/2023
A collection of simple classification functions
'''
import datetime # for classifying year
import re # Regular Expressions: powerful but difficult to use correctly

# define my regular expressions
only_letters = re.compile(r'[A-Za-z]*')
NNNN_NN_NN = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')


def is_word(word_candidate):
    return bool( only_letters.fullmatch(word_candidate) )


def is_int(integer_candidate):
    try:
        integer_candidate = int(integer_candidate)
    except ValueError:
        return False
    return isinstance(integer_candidate, int)


def is_decimal(decimal_candidate):
    try:
        decimal_candidate = float(decimal_candidate)
    except ValueError:
        return False
    return isinstance(decimal_candidate, float)


def is_date(date_candidate):
    # as long as ####-##-## format
    if bool( NNNN_NN_NN.fullmatch(date_candidate) ):
        ## verify month and Day arent too large
        try:
            datetime.datetime.strptime(date_candidate, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    # otherwise return false
    return False


def classify(row):
    # takes in a row and returns a string classification
    
    candidate = row["to_classify"]
    
    if is_int(candidate):
        return "whole number"
    
    if is_decimal(candidate):
        return "decimal number"
    
    if is_date(candidate):
        return "date"
    
    if is_word(candidate):
        return "all letters"
    
    return "no clue"
