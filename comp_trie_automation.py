from lev_trie_gen import *
from lev_dfa_gen import *
from lib.util.timer import Timer  

corpus_trie = load_data(corpus_trie_path)
corpus_dfa = load_data(corpus_dfa_path)

print(corpus_trie.stats())
# max edit edistance
k = 3

timer = Timer()

# tests = ["food"]
tests = ["beautiful", "bad", "heart", "universty"]
ks    = list(range(1, k + 1))


lev_dfa   = LevTrieDFAGenerator(corpus_dfa)
lev_trie   = LevTrieGenerator(corpus_trie)


for w in tests:
    for k in ks:
        print("\nvalidating [{:10}] on k = {}".format(w, k))
        timer.start("Lev-Automation")
        dfa_result = lev_dfa.gen_candidates(w, k)
        timer.stop_and_report("Lev-Automation")


        timer.start("Lev-Trie")
        trie_result = lev_trie.gen_candidates(w, k)
        timer.stop_and_report("Lev-Trie")

        
        dfa_result = set(dfa_result)
        trie_result = set(trie_result)
        assert(dfa_result == trie_result)


        # print("Naive: {}".format(naive_result))
        # print("Lev:   {}".format(lev_result))
        # for w in naive_result:
            # if w not in lev_result:
                # raise Exception("{} in Naive but not in Lev!".format(w))

print("--------- Passed ---------")

