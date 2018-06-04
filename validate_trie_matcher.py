from lev_trie_gen import *
from lib.util.timer import Timer  
from naive_gen import *

import random

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

words = read_dict(corpus_path) # corpus for picking out random words
def generate_tests(num_tests, edit_probability = 0.0):
    # num_tests: int that specifies the number of test words to generate
    # edit_probability: for each word, the probability that we'll do an edit on it
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # used to get character for random insert/substitute

    tests = random.sample(words, num_tests)

    for i in range(len(tests)): # potentially carry out edits on each word
        test = tests[i]
        if random.random() < edit_probability:
            edit_idx = random.randint(0, len(test)-1) # position the edit's going to be at
            edit_type = random.random() # insert, delete, or substitute
            if edit_type < 1/3: # insert
                tests[i] = test[:edit_idx]+alphabet[random.randint(0, 25)]+test[edit_idx:]
            elif edit_type < 2/3: # delete
                tests[i] = test[:edit_idx]+test[edit_idx+1:]
            else: # substitute
                tests[i] = test[:edit_idx]+alphabet[random.randint(0, 25)]+test[edit_idx+1:]

    return tests

timer = Timer()

# tests = ["food"]
tests = ["beautiful", "bad", "heart", "universty"]
# tests = generate_tests(5, edit_probability=0.1)
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

