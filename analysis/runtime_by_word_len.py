# runtime analysis with varing word length 
import sys
sys.path.append("../")
from helper import * 
from util import * 
from config import * 
from naive_gen import * 
from lev_trie_gen import * 

words = ["m", "ti", "foo", "good", "email", "pretty", "manager", "perfectt", "wonderful", "university"]
print(list(len(x) for x in words))

corpus_trie = load_data(corpus_trie_path)
corpus_ht  = load_data(corpus_hash_path)

naive_generator = NaiveGenerator(corpus_ht)
lev_generator   = LevTrieGenerator(corpus_trie)

k = 2

naive = get_runtime_by_word_len(k, words, naive_generator)
print("naive:  {}".format(naive))

lev = get_runtime_by_word_len(k, words, lev_generator)
print("lev:    {}".format(lev))
