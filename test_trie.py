from trie import *
from util import *

# words = ["aa"]
# words = ["aa", "abc"]
# words = ["a", "aa", "abc", "cc", "fff", "ffffa", "aaa", "abc"]
# words = ["fff", "ffffa"]
words = get_web_dictionary()
trie = Trie(words)
print(trie.stats())
# print(trie)
trie.to_patria_trie()
print("---- Compressed --- ")
# print(trie.stats())
# print(trie)
save_data(trie, "./data/pickle/web2_patricia_trie.pkl")
# save_data(trie, "./data/pickle/web2_trie.pkl")
