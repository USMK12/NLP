import nltk
from nltk.tokenize import word_tokenize

# Download the necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input text
text = "Everything is all about money."

# Tokenize the text
tokens = word_tokenize(text)

# Perform part-of-speech tagging
tagged = nltk.pos_tag(tokens)

# Print the tagged tokens
print(tagged)
