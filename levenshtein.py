from automata.fa.dfa import *
from automata.fa.nfa import *

class Levenshtein:


    def __init__(self, word, k):
        """
        Args:
            word:
            k   : max edit distance 

        Return: 
        """
        for i, ch in enumerate(word):
            # k
