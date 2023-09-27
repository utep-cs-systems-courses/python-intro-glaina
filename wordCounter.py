#!/usr/bin/env python3

import sys
import re
import os
from collections import defaultdict

# use file as input
def read_file(infile):
  words = []

  with open(infile, 'r') as file:
    text = file.read()
    words = text.split()

  return words

# record each unique word and teh number of times it occurs
def word_count(inFile, outFile):
  words = read_file(inFile)
  count = defaultdict(int)

  for word in words:
    # convert word to lower (case-insensitive)
    word = word.lower()
    
    # Remove leading punctuation
    word = re.sub(r'^[^\w\s]+', '', word)
    
    # Remove trailing punctuation
    word = re.sub(r'[^\w\s]+$', '', word)
    
    count[word] += 1

  #sort words alphabetically
  sortWords = list(count.keys())
  sortWords.sort()

  with open(outFile, 'w') as f:
    for word in sortWords:
      tempstr = word + ': ' + str(count[word])
      f.write(tempstr + '\n')
      print(tempstr)

  return outFile

if __name__ == "__main__":
  if (len(sys.argv) != 3):
    print("Incorrect number of arguments. Please try again.")
    sys.exit(1)

  inputFile = sys.argv[1]
  outputFile = sys.argv[2]

  word_count(inputFile, outputFile)
