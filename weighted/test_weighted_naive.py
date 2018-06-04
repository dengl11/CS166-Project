import sys
sys.path.append("../")
from util import *
from trie import *
from levenshtein import * 
from match import * 
from config import * 
from generator import * 
from weighted_naive_gen import *

# [c_insert, c_delete, c_subs]
weighted_cost = [2, 2, 3]

w = "foad"
k = 3

corpus_ht      = corpus2set(corpus_path) 
weighted_naive = WeightedNaiveGenerator(weighted_cost, corpus_ht)
print(weighted_naive.gen_candidates(w, k))
