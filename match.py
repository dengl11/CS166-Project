from util import *

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

