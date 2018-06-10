# fsm.py - http://www.graphviz.org/content/fsm
import sys
sys.path.append("../")
from lib.util.plotter import * 
from levenshtein import *  
import re

from graphviz import Digraph


def draw_lev_nfa(word, k, **kargs):
    """
    Args:
        NFA: 

    Return: 
    """ 
    f = Digraph('finite_state_machine', filename=kargs.get("fname", "nfa"))
    f.attr(rankdir='LR', size='5') 
    n = len(word)
    accepted = kargs.get("accepted", {})
    # accepted states 
    for i in range(n + 1):
        for j in range(k+1):
            shape = "doublecircle" if i == n else "circle"
            penwidth = "4" if i == n in accepted else "1.6" 
            style =  "filled" if (i, j) in accepted else ""
            color =  green if (i, j) in accepted else black
            f.node(str((i, j)), color = color, penwidth = penwidth, style=style, fontsize = "20", shape = shape, pos = "{},{}!".format(i*10, j*10))
    # transitions 
    f.attr('node', shape='circle')
    for i in range(n + 1):
        for j in range(k + 1):
            if j < k: # up 
                f.edge(str((i, j)), str((i, j + 1)), label="*", fontsize="20", color=blue, penwidth="2")
            if i < n: # ->
                f.edge(str((i, j)), str((i + 1, j)), label=word[i], fontsize="30", penwidth="2")
            if i < n and j < k: # diag 
                f.edge(str((i, j)), str((i + 1, j + 1)), label="*", fontsize="24", color=light_purple, penwidth="2")
                f.edge(str((i, j)), str((i + 1, j + 1)), label="<&#949;>", fontsize = "24", color="red", penwidth="2")
    f.format = kargs.get("format", "svg")
    f.rotate = 180
    f.render()



def render_dfa_walker(lev_w, w, k):
    """walk dfa on string w
    Args:
        dfa: 

    Return: 
    """
    outputs = []
    step = 0
    dfa = construct_levenshten(lev_w, k)
    s = dfa.initial_state
    acc_s = ""
    for i, ch in enumerate(w):
        fname = "{}_{}_{}_{}".format(lev_w, w, k, step)
        s = dfa.transitions[s][ch]
        acc_s += ch 
        next_states = eval(s)
        if not next_states:
            outputs.append((acc_s, None))
            return outputs 
        draw_lev_nfa(lev_w, k, fname = fname, accepted = next_states)
        outputs.append((acc_s, fname))
        step += 1
    if s not in dfa.final_states:
        outputs.append((acc_s, None))
    return outputs

