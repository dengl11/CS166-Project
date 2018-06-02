import math
from Datum import Datum
from Sentence import Sentence
from HolbrookCorpus import HolbrookCorpus
from StupidBackoffLanguageModel import StupidBackoffLanguageModel
from EditModel import EditModel
from SpellingResult import SpellingResult
import types

# Modified version of Peter Norvig's spelling corrector
"""Spelling Corrector.

Copyright 2007 Peter Norvig. 
Open source code under MIT license: http://www.opensource.org/licenses/mit-license.php
"""

import re, collections

class SpellCorrect:
  """Spelling corrector for sentences. Holds edit model, language model and the corpus."""

  def __init__(self, lm, corpus):
    self.languageModel = lm
    self.editModel = EditModel('data/count_1edit.txt', corpus)

  def correctSentence(self, sentence):
    """Assuming exactly one error per sentence, returns the most probable corrected sentence.
       Sentence is a list of words."""

    if len(sentence) == 0:
      return []

    bestSentence = sentence[:] #copy of sentence
    bestScore = float('-inf')
    
    for i in range(1, len(sentence) - 1): #ignore <s> and </s>
      # TODO: select the maximum probability sentence here, according to the noisy channel model.
      # Tip: self.editModel.editProbabilities(word) gives edits and log-probabilities according to your edit model.
      #      You should iterate through these values instead of enumerating all edits.
      # Tip: self.languageModel.score(trialSentence) gives log-probability of a sentence
      edit_probabilities = self.editModel.editProbabilities(sentence[i])
      for word, probability in edit_probabilities:
        trialSentence = sentence[:]
        trialSentence[i] = word
        trialScore = self.languageModel.score(trialSentence)+probability
        if trialScore>bestScore:
          bestScore = trialScore
          bestSentence = trialSentence

    return bestSentence

  def evaluate(self, corpus):  
    """Tests this speller on a corpus, returns a SpellingResult"""
    numCorrect = 0
    numTotal = 0
    testData = corpus.generateTestCases()
    for sentence in testData:
      if sentence.isEmpty():
        continue
      errorSentence = sentence.getErrorSentence()
      hypothesis = self.correctSentence(errorSentence)
      if sentence.isCorrection(hypothesis):
        numCorrect += 1
      numTotal += 1
    return SpellingResult(numCorrect, numTotal)

  def correctCorpus(self, corpus): 
    """Corrects a whole corpus, returns a JSON representation of the output."""
    string_list = [] # we will join these with commas,  bookended with []
    sentences = corpus.corpus
    for sentence in sentences:
      uncorrected = sentence.getErrorSentence()
      corrected = self.correctSentence(uncorrected)
      word_list = '["%s"]' % '","'.join(corrected)
      string_list.append(word_list)
    output = '[%s]' % ','.join(string_list)
    return output

def main():
  """Trains all of the language models and tests them on the dev data. Change devPath if you
     wish to do things like test on the training data."""
  trainPath = 'data/holbrook-tagged-train.dat'
  trainingCorpus = HolbrookCorpus(trainPath)

  devPath = 'data/holbrook-tagged-dev.dat'
  devCorpus = HolbrookCorpus(devPath)

  print('Stupid Backoff Language Model: ')
  sbLM = StupidBackoffLanguageModel(trainingCorpus)
  sbSpell = SpellCorrect(sbLM, trainingCorpus)
  sbOutcome = sbSpell.evaluate(devCorpus)
  print(str(sbOutcome))

if __name__ == "__main__":
    main()
