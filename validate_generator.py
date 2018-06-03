from lev_gen import *
from naive_gen import *
from lib.util.timer import Timer  
DEBUG = False
# DEBUG = True


if DEBUG:
    corpus_dfa = corpus2dfa(corpus_path)
    corpus_ht  = corpus2set(corpus_path) 
else:
    corpus_dfa = load_data(corpus_dfa_path)
    corpus_ht  = load_data(corpus_hash_path)

k = 3

# tests = ["food"]
tests = ["beautiful", "bad", "heart"]
ks    = list(range(1, k + 1))

naive_generator = NaiveGenerator(corpus_ht)
lev_generator   = LevTrieGenerator(corpus_dfa)

timer = Timer()

for w in tests:
    for k in ks:
        print("\nvalidating {} on k = {}".format(w, k))
        timer.start("Naive")
        naive_result = naive_generator.gen_candidates(w, k)
        timer.stop_and_report("Naive")

        timer.start("Lev")
        lev_result = lev_generator.gen_candidates(w, k)
        timer.stop_and_report("Lev")

        naive_result = set(naive_result)
        lev_result = set(lev_result)
        assert(naive_result == lev_result)

        # print("Naive: {}".format(naive_result))
        # print("Lev:   {}".format(lev_result))
        # for w in naive_result:
            # if w not in lev_result:
                # raise Exception("{} in Naive but not in Lev!".format(w))

print("--------- Passed ---------")

