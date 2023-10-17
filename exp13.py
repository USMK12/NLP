from lark import Lark

# Define the context-free grammar
grammar = '''
    start: sentence
    sentence: "the" noun "is" adjective
    noun: "cat" | "dog" | "bird"
    adjective: "happy" | "sad" | "hungry"
'''

# Create the parser
parser = Lark(grammar, start='start')

# Parse a sentence and generate the parse tree
sentence = "the cat is happy"
tree = parser.parse(sentence)

# Print the parse tree
print(tree.pretty())
