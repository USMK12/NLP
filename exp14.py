import nltk

# Define the context-free grammar
grammar = nltk.CFG.fromstring("""
    S -> NP[AGR=?n] VP[AGR=?n]
    NP[AGR=?n] -> PropN[AGR=?n]
    VP[TENSE=?t, AGR=?n] -> Cop[TENSE=?t, AGR=?n] Adj
    Cop[TENSE=pres, AGR=[NUM=sg, PER=3]] -> 'is'
    PropN[AGR=[NUM=sg, PER=3]] -> 'Kim'
    Adj -> 'happy'
""")

# Create a feature-based chart parser
parser = nltk.FeatureChartParser(grammar)

# Input sentence
sentence = "Kim is happy"

# Tokenize the sentence
tokens = sentence.split()

# Parse the sentence
for tree in parser.parse(tokens):
    print(tree)
    tree.pretty_print()
