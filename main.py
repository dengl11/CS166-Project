from util import *
from trie import *

# edits1 = read_train_data()
# print("Edits1 has {} entries ".format(len(edits1)))

web2 = get_web_dictionary()
trie = Trie(web2)
print(trie.stats())

