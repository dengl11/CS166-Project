import sys
sys.path.append("../")
from lib.util.plotter import *
from weighted_lev_gen import *

from graphviz import Digraph

# [c_insert, c_delete, c_subs]
weighted_cost = [1, 2, 3]

w = "data"
k = 3

def draw_weighted_lev_nfa(word, k, **kargs):
    """
    Args:
        NFA:

    Return:
    """
    lev = WeighedLevTrieGenerator(weighted_cost, {})
    nfa = lev.construct_levenshten_nfa(word, k)
    f = Digraph('finite_state_machine', filename=kargs.get("fname", "nfa"))
    f.attr(rankdir='LR', size='5')
    n = len(word)
    for s in nfa.states:
        i , j = eval(s)
        accepted = s in nfa.final_states 
        shape = "doublecircle" if accepted else "circle"
        penwidth = "4" if accepted else "1.6"
        style =  "filled" if accepted else ""
        color =  green if accepted else black
        f.node(str((i, j)), color = color, penwidth = penwidth, style=style, fontsize = "20", shape = shape)
    # transitions
    f.attr('node', shape='circle')
    for s in nfa.states:
        i, e = eval(s)
        remain = k - e
        if remain >= lev.c_insert:
            f.edge(s, str((i, e + lev.c_insert)), label="*", fontsize="30", color=blue, penwidth="2")
        if i >= n: continue
        f.edge(s, str((i + 1, e)), label=word[i], fontsize="30", penwidth="2")
        if remain >= lev.c_subs:
            f.edge(s, str((i + 1, e + lev.c_subs)), label="*", fontsize="30", color=light_purple, penwidth="2")
        if remain >= lev.c_delete:
            f.edge(s, str((i + 1, e + lev.c_delete)), label="<&#949;>", fontsize="20", color=red, penwidth="2")


    f.format = kargs.get("format", "svg")
    f.render()


draw_weighted_lev_nfa(w, k, fname = "weighted_dfa")
