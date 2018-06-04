# Trie Data Structure
# ---------------------------------------------------------------------------
# Reference:
# - https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python\
#       ?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

import sys
from pprint import pprint 
from collections import defaultdict
from util import * 
# lib: https://github.com/caleb531/automata
from automata.fa.dfa import *
from automata.fa.nfa import *


TERMINATE = "$"

def corpus2trie(corpus_path):
    """
    return {word} as a Trie object
    """
    words = read_dict(corpus_path)
    return Trie(words)
        
class Trie:
    root        = {}
    n_words     = 0
    n_nodes     = 1 
    is_patricia = False 

    def __init__(self, words):
        """construct a trie for a dictionary of words
        Args:
            words: [word] 

        Return: 
        """
        root = dict() # root of trie 
        self.n_words = len(words)
        for w in words:
            curr = root
            for i, ch in enumerate(w):
                if ch not in curr:
                    self.n_nodes += 1
                    curr[ch] = {}
                # accepting? 
                if i == len(w) - 1:
                    curr[ch][TERMINATE] = True 
                curr = curr[ch]
        self.root = root

    def stats(self):
        """
        Args:

        Return: 
        """
        s =  "Number of words: {:10}\n".format(self.n_words)
        s += "Number of nodes: {:10}\n".format(self.n_nodes) 
        return s



    def __str__(self):
        """print a trie in a pretty way
        Args:
            trie: multi-level dictionary

        Return: 
        """
        s = ""
        stack = []
        for ch, children in self.root.items():
            stack.append((ch, children, 0))

        while stack:
            ch, children, depth = stack.pop()
            accepted = children.get(TERMINATE, False) 
            if accepted: 
                s += ("{} -({})\n".format("  "*depth, ch))
            else: 
                s += ("{} - {} \n".format("  "*depth, ch))
            depth += 1
            for c, cc in children.items():
                if (c == TERMINATE): continue 
                stack.append((c, cc, depth))
        return s 

    def to_DFA(self):
        """construct a DFA from a trie

        Return: a DFA object 
        """
        initial_state = "^"
        states = {initial_state}
        final_states = set()
        transitions = defaultdict(dict)

        queue = [(initial_state, self.root)]
        state = 0
        while queue:
            k, children = queue.pop(0)
            if (children.get(TERMINATE, False)):
                final_states.add(k)
                
            for c, cc in children.items():
                if (c == TERMINATE): continue 
                c_state = k + c
                states.add(c_state)
                transitions[k][c] = {c_state}
                queue.append((c_state, cc))

        nfa = NFA(states = states,\
                   transitions = transitions,\
                   initial_state = initial_state,\
                   final_states = final_states,\
                   input_symbols = set(ALPHABETS))
        return DFA.from_nfa(nfa)

    def accept(self, node):
        """return true if ndoe is accepted 
        Args:
            node: {}

        Return: 
        """
        return TERMINATE in node


    def to_patria_trie(self, verbose = True):
        """compress into a patria trie
        Return: 
        """
        ans = defaultdict(dict) 
        self.n_nodes = 0
        # [(parent, key, node)]
        stack = list((ans, k, v) for (k, v) in self.root.items()) 
        while stack:
            parent, key, node = stack.pop()
            if (key == TERMINATE): 
                parent[key] = node
                continue 

            acc_key = key  # accumulative key
            while len(node.keys()) == 1 and TERMINATE not in node: # silly and non-terminal node
                k, node = node.popitem()
                acc_key += k 
            
            # pop old key from parent
            parent.pop(key, None)

            parent[acc_key] = node 
            self.n_nodes += 1
            for k, v in node.items():
                if k == TERMINATE: continue 
                stack.append((node, k, v))
        if verbose:
            print("Trie Compressed: {} -> {}".format(sys.getsizeof(self.root), sys.getsizeof(ans)))
        self.root = ans 
        self.is_patricia = True 





