class SimWordGenerator:
    """ interface class for candidiate generator """

    def gen_candidates(self, w, k):
        """get candidates of w within edit distance of k
        Args:
            w: 

        Return: [candidate]
        """
        raise Exception("Should be implemented by child class!")
