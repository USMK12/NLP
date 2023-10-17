from pcfg import PCFGParser

# Load the pre-trained PCFG model
parser = PCFGParser('counts_file.sample')

# Define the sentence to parse
sentence = "the man saw the dog with the telescope"

# Parse the sentence and get the parsed tree
parsed_tree = parser.parse(sentence)

# Print the parsed tree
print(parsed_tree)
