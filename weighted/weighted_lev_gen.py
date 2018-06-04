import sys, os

sys.path.append(os.path.join(os.path.abspath(__file__), "../"))
from util import *
from trie import *
from levenshtein import * 
from match import * 
from generator import * 
from config import * 
from lev_dfa_gen import *   
from weighted_gen import *   

class WeighedLevTrieGenerator(LevTrieDFAGenerator):

    def __init__(self, costs, corpus_dfa = None):
        self.corpus_dfa = corpus_dfa or load_data(corpus_dfa_path)
        WeightedGenerator.__init__(self, costs)

    def construct_levenshten(self, word, k):
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
            ch = word[i] if (i < n) else None
            for e in range(k + 1):
                credit = k - e # remaining credits 
                curr  = m[(i, e)]
                right = m[(i + 1, e)] if ch else None 
                if credit >= self.c_insert: # can insert  
                    up = m[(i, e + self.c_insert)] 
                    for c in ALPHABETS: transitions[curr][c].add(up)
                    
                if not right: continue

                transitions[curr][ch].add(right)  # correct char: right arrow 

                if credit >= self.c_delete: # can delete   
                    next_del = m[(i + 1, e + self.c_delete)]
                    transitions[curr][""].add(next_del)  # deletions -  epsilon: diagonal arrow 

                if credit < self.c_subs: continue 
                next_subs = m[(i + 1, e + self.c_subs)]
                for c in ALPHABETS:
                    transitions[curr][c].add(next_subs
)

        nfa = NFA(states = set(m.values()),\
                  transitions = transitions,\
                  initial_state = m[(0, 0)],\
                  final_states = {m[(n, j)] for j in range(k + 1)},\
                  input_symbols = set(ALPHABETS))
        return DFA.from_nfa(nfa)


    def gen_candidates(self, w, k):
        """get candidates of w within edit distance of k
        Args:
            w: 

        Return: 
        """
        lev_dfa = self.construct_levenshten(w, k)
        return list(match(self.corpus_dfa, lev_dfa))
