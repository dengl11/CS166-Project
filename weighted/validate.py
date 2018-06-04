import sys
sys.path.append("../")
from util import *
from trie import *
from levenshtein import * 
from lib.util.timer import Timer  
from match import * 
from config import * 
from generator import * 
from weighted_naive_gen import *
from weighted_lev_gen import * 

DEBUG = False
# DEBUG = True

if DEBUG: # if debug, user a toy dataset 
    corpus_dfa = corpus2dfa(corpus_path)
    corpus_ht  = corpus2set(corpus_path) 
else:
    corpus_dfa = load_data(corpus_dfa_path)
    corpus_ht  = load_data(corpus_hash_path)


# [c_insert, c_delete, c_subs]
weighted_cost = [1, 2, 3]

k = 5

tests = ["beautiful", "bad", "heart"]
ks    = list(range(1, k + 1))

timer = Timer()

weighted_lev = WeighedLevTrieGenerator(weighted_cost, corpus_dfa)

weighted_naive = WeightedNaiveGenerator(weighted_cost, corpus_ht)

for w in tests:
    for k in ks:
        print("\nvalidating [{:10}] on k = {}".format(w, k))
        timer.start("Lev")
        lev_result = weighted_lev.gen_candidates(w, k)
        timer.stop_and_report("Lev")

        timer.start("Naive")
        naive_result = weighted_naive.gen_candidates(w, k)
        timer.stop_and_report("Naive")

        naive_result = set(naive_result)
        lev_result = set(lev_result)
        assert(naive_result == lev_result)

        # print("Naive: {}".format(naive_result))
        # print("Lev:   {}".format(lev_result))
        # for w in naive_result:
            # if w not in lev_result:
                # raise Exception("{} in Naive but not in Lev!".format(w))

print("--------- Passed ---------")


