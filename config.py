import os 

repo_path = os.path.dirname(os.path.abspath(__file__))

# [c_insert, c_delete, c_subs]
weighted_cost = [1, 2, 3]

corpus_hash_path = os.path.join(repo_path, "./data/pickle/web2_hash.pkl" )
corpus_dfa_path = os.path.join(repo_path, "./data/pickle/web2_automation.pkl")
corpus_trie_path = os.path.join(repo_path, "./data/pickle/web2_trie.pkl")

corpus_path = os.path.join(repo_path, "./data/toy/food")
# corpus_path = "./data/toy/boat"
