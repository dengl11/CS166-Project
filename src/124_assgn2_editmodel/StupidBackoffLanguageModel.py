import math

class StupidBackoffLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    self.bigram_dict = dict()
    self.counts_dict = dict()
    self.word_count = 0
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """
    # Tip: To get words from the corpus, try
    #    for sentence in corpus.corpus:
    #       for datum in sentence.data:  
    #         word = datum.word
    for sentence in corpus.corpus:
      words = []

      # increment unigram counts
      for datum in sentence.data: 
        word = datum.word
        words.append(word) # less messy way to get bigrams
        self.word_count += 1
        self.counts_dict[word] = self.counts_dict.get(word, 1)+1 # defaults to 1 for add-one smoothing
      
      # increment bigram counts
      for bigram in zip(words[:-1], words[1:]):
        self.bigram_dict[bigram] = self.bigram_dict.get(bigram, 0)+1

    self.counts_dict['UNK'] = 1

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    sentence = [word if word in self.counts_dict else 'UNK' for word in sentence]
    log_probability = 0
    for bigram in zip(sentence[:-1], sentence[1:]):
      if bigram in self.bigram_dict:
        log_probability += math.log(self.bigram_dict[bigram])-math.log(self.counts_dict[bigram[0]])
      else:
        if not bigram[1] == '</s>':
          log_probability += math.log(0.4*self.counts_dict[bigram[1]]/self.word_count)
    return log_probability
