import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet

# Define the sentence
sentence = "The cat sat on the mat."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Perform POS tagging
pos_tags = pos_tag(tokens)

# Extract noun phrases
noun_phrases = []
current_noun_phrase = []
for word, pos in pos_tags:
    if pos.startswith('NN'):
        current_noun_phrase.append(word)
    else:
        if current_noun_phrase:
            noun_phrases.append(' '.join(current_noun_phrase))
            current_noun_phrase = []
if current_noun_phrase:
    noun_phrases.append(' '.join(current_noun_phrase))

# Determine the meaning of the noun phrases
for noun_phrase in noun_phrases:
    synsets = wordnet.synsets(noun_phrase)
    if synsets:
        print(noun_phrase, synsets[0].definition())
