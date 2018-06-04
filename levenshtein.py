from collections import defaultdict
from pprint import pprint 
from automata.fa.dfa import *
from automata.fa.nfa import *
from util import *
from trie import * 

def corpus2dfa(corpus_path):
    """
    Args:
        corpus_path: 

    Return: 
    """
    words = read_dict(corpus_path)
    trie = Trie(words)
    return trie.to_DFA()

def construct_levenshten_nfa(word, k):
    """
    Args:
        word:
        k   : max edit distance 

    Return: 
    """
    n = len(word)
    m = dict() # {(n_char, n_err): state_name}
    for nc in range(n + 1):
        for ne in range(k + 1):
            m[(nc, ne)] = str((nc, ne))
    transitions = defaultdict(lambda: defaultdict(lambda: set()))
    for i in range(n + 1): 
        for e in range(k + 1):
            curr  = m[(i, e)]
            right = m[(i + 1, e)] if (i < n) else None
            if right:
                transitions[curr][word[i]].add(right)  # correct char: right arrow 
            if e >= k: continue 
            # non-top states 
            up        = m[(i    , e + 1)] 
            if right:
                top_right = m[(i + 1, e + 1)]
                transitions[curr][""].add(top_right)  # deletions -  epsilon: diagonal arrow 
            for ch in ALPHABETS:
                # insertions: upward arrow + subsitutions: diagonal arrow 
                transitions[curr][ch].add(up)
                if (top_right):
                    transitions[curr][ch].add(top_right)

    nfa = NFA(states = set(m.values()),\
              transitions = transitions,\
              initial_state = m[(0, 0)],\
              final_states = {m[(n, j)] for j in range(k + 1)},\
              input_symbols = set(ALPHABETS))
    return nfa 


def construct_levenshten(word, k):
    nfa = construct_levenshten_nfa(word, k)
    return DFA.from_nfa(nfa)
