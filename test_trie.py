from trie import *

# words = ["aa"]
# words = ["aa", "abc"]
words = ["a", "aa", "abc", "cc", "fff", "ffffa", "aaa", "abc"]
# words = ["fff", "ffffa"]
trie = Trie(words)
print(trie.stats())
print(trie)
trie.to_patria_trie()
print("---- Compressed --- ")
print(trie)
