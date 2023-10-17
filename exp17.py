import nltk
from nltk.corpus import wordnet

# Download WordNet if not already downloaded
nltk.download('wordnet')

# Define a word
word = 'business'

# Get the synsets for the word
synsets = wordnet.synsets(word)

# Print information about each synset
for synset in synsets:
    print('Synset name:', synset.name())
    print('Lemmas:', synset.lemmas())
    print('Definition:', synset.definition())
    print('Example:', synset.examples())
    print()
