import nltk
nltk.download('punkt')  
from nltk.parse.earleychart import EarleyChartParser  
from nltk import Tree  
parser = EarleyChartParser()
sentence = "The cat chased the mouse."
for tree in parser.parse(sentence.split()):
    tree.pretty_print()
