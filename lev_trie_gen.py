from util import *
from trie import *
from levenshtein import * 
from match import * 
from generator import * 
from config import * 

class LevTrieGenerator(SimWordGenerator):
    """
    Levenshtein Automation + Trie 
    """ 

    def __init__(self, corpus_trie = None):
        self.corpus_trie = corpus_trie or corpus2trie(corpus_dfa_path)

    def gen_candidates(self, w, k):
        """get candidates of w within edit distance of k
        Args:
            w: 

        Return: 
        """
        lev_dfa = construct_levenshten(w, k)
        return list(match_lv_trie(lev_dfa, self.corpus_trie))
