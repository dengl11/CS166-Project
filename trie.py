# Trie Data Structure
# ---------------------------------------------------------------------------
# Reference:
# - https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python\
#       ?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

import string
from pprint import pprint 
from collections import defaultdict
from util import * 
# lib: https://github.com/caleb531/automata
from automata.fa.dfa import *
from automata.fa.nfa import *


TERMINATE = "$"
ALPHABETS = list(string.ascii_lowercase)

# class TrieNode:
    # ch = ''
    # accepted = False  # is terminating node for a word 
    # children = []   

    # def __init__(self, ch, accepted = False):
        # self.ch = ch
        # self.accepted = accepted 

        
class Trie:
    root = {}
    n_words = 0
    n_nodes = 1 

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
                # print("word: {} | ch: {} | i: {}".format(w, ch, i))
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
        states = {'q{}'.format(i) for i in range(self.n_nodes)}
        initial_state = "q0"
        final_states = set()
        transitions = defaultdict(dict)

        queue = [("q0", self.root)]
        state = 0
        while queue:
            k, children = queue.pop(0)
            if (children.get(TERMINATE, False)):
                final_states.add(k)
                
            for c, cc in children.items():
                if (c == TERMINATE): continue 
                state += 1
                c_state = "q{}".format(state)
                transitions[k][c] = {c_state}
                queue.append((c_state, cc))

        # pprint(states)
        # pprint(transitions)
        # pprint(final_states)
        print("DFA Start")
        print_now()
        nfa = NFA(states = states,\
                   transitions = transitions,\
                   initial_state = initial_state,\
                   final_states = final_states,\
                   input_symbols = set(ALPHABETS))
        print("DFA Done")
        print_now()
        return DFA.from_nfa(nfa)
