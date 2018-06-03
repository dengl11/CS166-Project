# utility script
   
import string
import datetime, time
import pickle

ALPHABETS = list(string.ascii_lowercase)
EMPTY_STATE = "{}"


def read_dict(path):
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
