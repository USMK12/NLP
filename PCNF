import nltk
from nltk import PCFG
from nltk import ChartParser
pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.7] | NP PP [0.3]
    VP -> V NP [0.4] | VP PP [0.3] | V [0.3]
    PP -> P NP [1.0]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'cat' [0.2] | 'dog' [0.2] | 'bat' [0.2] | 'rat' [0.2] | 'hat' [0.2]
    V -> 'chased' [0.5] | 'saw' [0.5]
    P -> 'in' [0.6] | 'on' [0.4]
""")
parser = ChartParser(pcfg_grammar)
sentence = "the cat chased the dog".split()
for tree in parser.parse(sentence):
    tree.pretty_print()
