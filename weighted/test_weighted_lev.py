import sys
sys.path.append("../")
from util import *
from trie import *
from levenshtein import * 
from match import * 
from config import * 
from generator import * 
from weighted_naive_gen import *
from weighted_lev_gen import * 

# [c_insert, c_delete, c_subs]
weighted_cost = [3, 4, 2]

w = "foood"
k = 3

corpus_dfa = corpus2dfa(corpus_path)
weighted_lev = WeighedLevTrieGenerator(weighted_cost, corpus_dfa)
weighted_lev.gen_candidates(w, k)
# print(weighted_lev.gen_candidates(w, k))

