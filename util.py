# utility script
   
import string
import datetime, time
import pickle

ALPHABETS = list(string.ascii_lowercase)
EMPTY_STATE = "{}"

def read_dict(path):
    """
    return [word]
    """
    ans = []
    with open(path) as f:
        for w in f.readlines():
            w = w.rstrip().lower() 
            # filter out non-alphabetic words
            if (not w.isalpha()): continue
            ans.append(w)
    return ans 
       
def read_train_data():
    pairs = []
    with open("./data/training_set/edit1s.txt") as f:
        for l in f.readlines():
            spelling, corrected = l.split('\t')
            pairs.append((spelling, corrected))
    return pairs


def get_web_dictionary():
    return read_dict("/usr/share/dict/web2")

def get_web_dictionary_set():
    """
    return {word} as a set 
    """
    return set(get_web_dictionary())

def print_now():
    ts = time.time()
    print(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))


def save_data(data, path):
    """save a data to path
    Args:
        data: 
        path: 

    Return: 
    """
    with open(path, "wb") as f:
        pickle.dump(data, f)

def load_data(path):
    """
    Args:
        path: 

    Return: 
    """
    with open(path, "rb") as f:
        return pickle.load(f)


def edits_1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for (L, R) in splits if R]
    subs    = [L + c + R[1:] for (L, R) in splits if R for c in ALPHABETS]
    inserts = [L + c + R for (L, R) in splits for c in ALPHABETS]
    return set(deletes + inserts + subs)

def edits_k(k, word):
    """generate candidates within k edit-distance of word
    Args:
        k: 

    Return: {word}
    Ref:
        https://norvig.com/spell-correct.html
    """
    ans = set([word])
    pre = set([word]) 
    for _ in range(k):
        curr = set() 
        for w in pre:
            curr |= edits_1(w)
        ans |= curr
        pre = curr 
    return ans 



def corpus2set(corpus_path):
    """
    return {word} as a set 
    """
    return set(read_dict(corpus_path))


def walk_dfa(dfa, w):
    """walk dfa on string w
    Args:
        dfa: 

    Return: 
    """
    print("-------------------")
    s = dfa.initial_state
    acc_s = ""
    for ch in w:
        print()
        print("before s: {}".format(s))
        s = dfa.transitions[s][ch]
        acc_s += ch 
        print("acc_s: {}".format(acc_s))
        print("after s: {}".format(s))
        print("Accepted: {}".format(s in dfa.final_states))
        print(dfa.final_states)
    print("-------------------")
