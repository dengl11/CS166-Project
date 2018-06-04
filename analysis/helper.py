
import sys
sys.path.append("../")
from lib.util.plotter import * 
from lib.util.timer import * 
import numpy as np 

timer = Timer()

def scale_down2d(data):
    """
    Args:
        data: 

    Return: 
    """
    return [[np.log(1 + x) for x in y] for y in data]

def scale_down(data):
    """
    Args:
        data: 

    Return: 
    """
    return [np.log(1 + x) for x in data]


def get_runtime_by_k(max_k, test_w, generator):
    """get a list of runtime for a list of k
    Args:
        max_k: 
        test_w: 
        generator: 

    Return: 
    """
    runtime = []
    for k in range(1, max_k + 1):
        timer.start("k")
        generator.gen_candidates(test_w, k)
        runtime.append(timer.stop("k"))
    return runtime 
    


def get_runtime_by_word_len(k, words, generator):
    """get a list of runtime for a list of k
    Args:
        max_k: 
        test_w: 
        generator: 

    Return: 
    """
    runtime = []
    for w in words:
        timer.start("k")
        generator.gen_candidates(w, k)
        runtime.append(timer.stop("k"))
    return runtime 
    

def get_runtime_2d(ks, words, generator):
    """get a list of runtime for a list of k
    Args:
        max_k: 
        test_w: 
        generator: 

    Return: 
    """
    runtime = []
    for w in words:
        curr = []
        for k in ks:
            timer.start("k")
            generator.gen_candidates(w, k)
            curr.append(timer.stop("k"))
        runtime.append(curr)
        print(w)
    return runtime 
    
