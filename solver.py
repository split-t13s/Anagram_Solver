import nltk
import re

from nltk.corpus import wordnet as wn

all_words = wn.all_lemma_names()
regexp = re.compile('^[A-Za-z]+$')      # Strings containing letters only

"""
Takes the list of all words and removes any word that does not match the
specified regular expression 'regexp'.
"""
def filter_all_words():    
    file = open("possiblewords.dat", "w")
    for word in all_words:
        result = regexp.search(word)
        if result != None:
            temp = word + "\n"
            file.write(temp)
    file.close()

