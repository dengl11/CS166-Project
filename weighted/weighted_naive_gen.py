import sys
sys.path.append("../")
from util import *
from trie import *
from levenshtein import * 
from match import * 
from config import *
from generator import * 
from naive_gen import * 
from weighted_gen import *   

        

class WeightedNaiveGenerator(NaiveGenerator, WeightedGenerator):


    def __init__(self, costs, corpus_dic = None):
        """
        costs: 
            [c_insert, c_delete, c_subs]
        """ 
        NaiveGenerator.__init__(self, corpus_dic)
        WeightedGenerator.__init__(self, costs)

    def edits1(self, word, credits):
        """generate candidates with just 1 operation on w with given credits
        Args:
            w: 
            credit: 

        Return: 
            [(curr_word, remain_credits)]
        """
        if (credits <= 0): return {}

        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = []
        subs    = []
        inserts = []
        if (credits >= self.c_delete):
            deletes = [(L + R[1:], credits - self.c_delete) for (L, R) in splits if R]
        if (credits >= self.c_subs):
            subs    = [(L + c + R[1:], credits - self.c_subs) for (L, R) in splits if R for c in ALPHABETS]
        if (credits >= self.c_insert):
            inserts = [(L + c + R, credits - self.c_insert) for (L, R) in splits for c in ALPHABETS]
        return deletes + inserts + subs


    def gen_candidates(self, w, k):
        """get candidates of w within edit distance of k
        Args:
            w: 

        Return:  {word}
        """
        ans = set()
        todo = [(w, k)] # stack of (word, remain_credits)
        added = set() # to prevent revisiting the same (s, c) pair 
        while todo:
            w, c = todo.pop()
            if w in self.corpus_dic: 
                ans.add(w)
            if (c == 0): continue 
            nexts = self.edits1(w, c)
            for p in nexts:
                if p not in added:
                    added.add(p)
                    todo.append(p)
        return ans 


