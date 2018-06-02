# Trie Data Structure
# ---------------------------------------------------------------------------
# Reference:
# - https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python\
#       ?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa


class Trie:
    root = {}
    n_words = 0
    n_nodes = 0 

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
            for ch in w:
                if ch not in curr:
                    self.n_nodes += 1
                    curr[ch] = {}
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
            s += ("{} - {}\n".format("  "*depth, ch))
            depth += 1
            for c, cc in children.items():
                stack.append((c, cc, depth))
        return s 
