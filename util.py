# utility script

def read_dict(path):
    with open(path) as f:
        return [w for w in f.readlines()]


def read_train_data():
    pairs = []
    with open("./data/training_set/edit1s.txt") as f:
        for l in f.readlines():
            spelling, corrected = l.split('\t')
            pairs.append((spelling, corrected))
    return pairs


def get_web_dictionary():
    return read_dict("/usr/share/dict/web2")

