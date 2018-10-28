import nltk
import re

from nltk.corpus import wordnet as wn

all_words = wn.all_lemma_names()
regexp = re.compile('^[A-Za-z]{3,}$')      # Strings with 3 or more letters

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
Returns words from all_words.dat that only contain letters from the list of
unique letters.
"""
def get_initial_words(unique_letters):
    file = open("all_words.dat", "r")
    file_as_lines = file.readlines()
    file.close()
    initial_words = []
    for line in file_as_lines:
        word = line[:-1]
        word_as_list = list(word)
        matched = 0
        for letter in word_as_list:
            for unique_letter in unique_letters:
                if letter == unique_letter:
                    matched += 1
        if matched == len(word_as_list):
            initial_words.append(word)
    return initial_words

"""
Filters words containing valid letters to words that contain upto the maximum
occurences of the valid letters.
"""
def get_final_words(initial_words, all_letters):
    dict_letters = letters_as_dict(all_letters)
    final_words = []
    for word in initial_words:
        word_as_list = list(word)
        match = 0
        for d_letter in dict_letters:   # Compare word to dictionary
            count = 0
            for letter in word_as_list:
                if d_letter == letter:
                    count += 1
                    match += 1          # Increment total letters word matches
                if count > dict_letters[d_letter]:
                    match = 0    # Stops inclusion of bad words
                    break
            else:
                continue
            break
        if match == len(word_as_list):  # Check matched is same as word
            final_words.append(word)
    return final_words
                        
"""
Sort list of words into descending size order
"""
def sort_big_to_small(words):
    words.sort(key=len, reverse=True)
    return words

"""
Takes a list of letters and returns a dictionary of the unique letters, where
the value is the number of times the same letter appears in the list.
"""
def letters_as_dict(letters):
    dict_letters = {}
    for letter in letters:
        if letter in dict_letters:
            dict_letters[letter] += 1
        else:
            dict_letters[letter] = 1
    return dict_letters

"""
Executes code in order
"""
def solve(letters):
    words = get_final_words(get_initial_words(get_unique_letters(letters)), letters)
    print(sort_big_to_small(words))


breaker = "utnspda"     # caused several errors, works correctly now

letters = "finish"      # fails to find hung, hung not in wordnet
solve(list(letters))

