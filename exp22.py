import nltk
from nltk.corpus import webtext
from neuralcoref import Coref

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Define the text
text = "John went to the store. He bought some milk."

# Parse the text
doc = nlp(text)

# Perform reference resolution
coref = Coref(nlp.vocab)
resolved_text = coref.one_shot_coref(text)

# Print the resolved text
print(resolved_text)
