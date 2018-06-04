from lev_trie_gen import *
from lib.util.timer import Timer  
from naive_gen import * 

DEBUG = False
# DEBUG = True

if DEBUG: # if debug, user a toy dataset 
    corpus_trie  = corpus2trie(corpus_path) 
    corpus_ht    = corpus2set(corpus_path) 
else:
    corpus_trie = load_data(corpus_trie_path)
    corpus_ht  = load_data(corpus_hash_path)

print(corpus_trie.stats())
# max edit edistance
k = 3

timer = Timer()

# tests = ["food"]
tests = ["beautiful", "bad", "heart", "universty"]
ks    = list(range(1, k + 1))

naive_generator = NaiveGenerator(corpus_ht)

lev_generator   = LevTrieGenerator(corpus_trie)


for w in tests:
    for k in ks:
        print("\nvalidating [{:10}] on k = {}".format(w, k))
        timer.start("Lev")
        lev_result = lev_generator.gen_candidates(w, k)
        timer.stop_and_report("Lev")


        timer.start("Naive")
        naive_result = naive_generator.gen_candidates(w, k)
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

