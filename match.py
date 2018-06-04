from util import *
from trie import *

def match_lv_trie(lv, trie):
    """match a Levenshtein DFA on corpus as a trie 
    Args:
        lv:      a Levenshtein DFA Object 
        trie:    a Trie object 

    Return: [accepted_word]
    """
    stack = [("", trie.root, lv.initial_state)]
    while stack:
        acc_s, trie_node, s2 = stack.pop()
        edges1 = set(trie_node.keys() )
        # print("\nedges1: {}".format(edges1))
        edges2 = lv.transitions[s2].keys()
        for ch in set(edges1).intersection(edges2):
            # print("ch = {}".format(ch))
            new_node = trie_node[ch]
            # print(new_node)
            new_s2 = lv.transitions[s2][ch]
            if new_node and new_s2 != EMPTY_STATE:
                new_acc_s = acc_s + ch
                # print("push: {}".format(new_node))
                stack.append((new_acc_s, new_node, new_s2))
                if trie.accept(new_node) and new_s2 in lv.final_states:
                    yield new_acc_s 


def match(corpus, lv):
    """match a Levenshtein DFA on corpus 
    Args:
        corpus:  a DFA Object 
        lv:      a Levenshtein DFA Object 

    Return: [accepted_word]
    """
    stack = [("", corpus.initial_state, lv.initial_state)]
    while stack:
        acc_s, s1, s2 = stack.pop()
        edges1 = corpus.transitions[s1].keys()
        edges2 = lv.transitions[s2].keys()
        for ch in set(edges1).intersection(edges2):
            new_s1 = corpus.transitions[s1][ch]
            new_s2 = lv.transitions[s2][ch]
            if new_s1 != EMPTY_STATE and new_s2 != EMPTY_STATE:
                new_acc_s = acc_s + ch
                stack.append((new_acc_s, new_s1, new_s2))
                if new_s1 in corpus.final_states and new_s2 in lv.final_states:
                    yield new_acc_s 

