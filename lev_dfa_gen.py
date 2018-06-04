from util import *
from trie import *
from levenshtein import * 
from match import * 
from generator import * 
from config import * 

class LevTrieDFAGenerator(SimWordGenerator):
    """
    Levenshtein Automation + Trie Automation 
    """ 

    def __init__(self, corpus_dfa = None):
        self.corpus_dfa = corpus_dfa or load_data(corpus_dfa_path)

    def gen_candidates(self, w, k):
        """get candidates of w within edit distance of k
        Args:
            w: 

        Return: 
        """
        lev_dfa = construct_levenshten(w, k)
        return list(match(self.corpus_dfa, lev_dfa))
