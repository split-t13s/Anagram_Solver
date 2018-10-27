import nltk
import re

from nltk.corpus import wordnet as wn

all_words = wn.all_lemma_names()
regexp = re.compile('^[A-Za-z]+$')      # Strings containing letters only

test_letters = ["b", "e", "t", "t", "e", "r"]

"""
Takes the list of all words and removes any word that does not match the
specified regular expression 'regexp'.
"""
def filter_all_words():    
    file = open("all_words.dat", "w")
    for word in all_words:
        result = regexp.search(word)
        if result != None:
            temp = word + "\n"
            file.write(temp)
    file.close()

"""
Returns all unique letters from a given list of letters.
"""
def get_unique_letters(letters):
    unique_letters = []
    for letter in letters:
        if letter not in unique_letters:
            unique_letters.append(letter)
    return unique_letters

"""
Returns words from all_words.dat that start with any unique letter from the list
of given letters.
"""
def get_initial_words(letters):
    unique_letters = get_unique_letters(letters)
    file = open("all_words.dat", "r")
    file_as_lines = file.readlines()
    file.close()
    initial_words = []
    for line in file_as_lines:
        for letter in unique_letters:
            if line.startswith(letter):
                initial_words.append(line)
                break
    return initial_words


