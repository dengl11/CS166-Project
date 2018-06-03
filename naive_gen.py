from util import *
from trie import *
from levenshtein import * 
from match import * 
from config import * 
from generator import * 


class NaiveGenerator(SimWordGenerator):

    """
    Naive Implementation fo Spell Checker Candidate Generator:
        All Constructions -> Hash Table
    """ 

    def __init__(self, corpus_dic = None):
        # self.words = get_web_dictionary_set()
        # save_data(words, corpus_hash_path)
        self.corpus_dic = corpus_dic or load_data(corpus_hash_path)


    def gen_candidates(self, w, k):
        """get candidates of w within edit distance of k
        Args:
            w: 

        Return: 
        """
        return [c for c in edits_k(k, w) if c in self.corpus_dic]
