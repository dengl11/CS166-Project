from util import *
from trie import *
from levenshtein import * 
from match import * 

use_toy = False 
# use_toy = True 

print_now()

corpus_dfa_path = "./data/pickle/web2.pkl"
if use_toy: 
    words = read_dict("./data/toy/mini")
    trie = Trie(words)
    corpus_dfa = trie.to_DFA()
    # save_data(corpus_dfa, corpus_dfa_path)
else:
    # words = get_web_dictionary()
    corpus_dfa = load_data(corpus_dfa_path)

test_word = "universiity"

lv = construct_levenshten(test_word, 1)
# print(list(lv.read_input_stepwise("foiod")))
# print(lv.final_states)
# print(corpus_dfa.final_states)

s = lv.initial_state
# acc_s = ""
# for ch in "fad":
    # s = lv.transitions[s][ch]
    # acc_s += ch 
    # print()
    # print("acc_s: {}".format(acc_s))
    # print("s: {}".format(s))
    # print(s in lv.final_states)
    # print(lv.final_states)


# s = corpus_dfa.initial_state
# for ch in test_word:
    # s = corpus_dfa.transitions[s][ch]
    # acc_s += ch 
    # print()
    # print(acc_s)
    # print(s in corpus_dfa.final_states)
# print(lv.transitions)

print(list(match(corpus_dfa, lv)))
