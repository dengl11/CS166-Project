# runtime analysis with varing k
import sys
sys.path.append("../")
from helper import * 
from util import * 
from config import * 
from naive_gen import * 
from lev_trie_gen import * 


corpus_trie = load_data(corpus_trie_path)
corpus_ht  = load_data(corpus_hash_path)

naive_generator = NaiveGenerator(corpus_ht)
lev_generator   = LevTrieGenerator(corpus_trie)

max_k = 3
test_w = "structre"
naive = get_runtime_by_k(max_k, test_w, naive_generator)
print("naive:  {}".format(naive))

lev = get_runtime_by_k(max_k, test_w, lev_generator)
print("lev:    {}".format(lev))
