# runtime analysis with varing k
import sys
sys.path.append("../")
sys.path.append("../weighted/")
from helper import * 
from util import * 
from config import * 
from generator import * 
from weighted_naive_gen import *
from weighted_lev_gen import * 


corpus_dfa = load_data(corpus_dfa_path)
corpus_ht  = load_data(corpus_hash_path)

# [c_insert, c_delete, c_subs]
weighted_cost = [1, 2, 1]

k = 2

tests = ["date", "book", "food", "pretty", "teacher"]
ks    = list(range(1, k + 1))

weighted_lev = WeighedLevTrieGenerator(weighted_cost, corpus_dfa)

weighted_naive = WeightedNaiveGenerator(weighted_cost, corpus_ht)


naive = get_runtime_2d(ks, tests, weighted_naive)
print("naive:  {}".format(naive))

lev = get_runtime_2d(ks, tests, weighted_lev)
print("lev:    {}".format(lev))
