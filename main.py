from util import *
from trie import *

# use_save = False 
use_save = True 
# edits1 = read_train_data()
# print("Edits1 has {} entries ".format(len(edits1)))

# web2 = get_web_dictionary()
# trie = Trie(web2)
# print(trie.stats())
print_now()

dfa_path = "./data/pickle/web2.pkl"
if not use_save: 
    # words = read_dict("./data/toy/mini")
    words = get_web_dictionary()
    trie = Trie(words)
    print(trie.stats())
# print(trie)
    dfa = trie.to_DFA()
    print("---- DFA Constructed ---- ")
    print_now()
    save_data(dfa, dfa_path)
else:
    dfa = load_data(dfa_path)

print("---- GO ---- ")
print_now()
print(list(dfa.read_input_stepwise("aa")))
print(list(dfa.read_input_stepwise("university")))
print(list(dfa.read_input_stepwise("bccc")))
print(list(dfa.read_input_stepwise("bcccc")))

