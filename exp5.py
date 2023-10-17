# Import the necessary modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Create an instance of the PorterStemmer class
ps = PorterStemmer()

# Define a list of words to be stemmed
words = ["program", "programs", "programmer", "programming", "programmers"]

# Perform stemming on each word in the list
stemmed_words = [ps.stem(w) for w in words]

# Print the original words and their stemmed forms
for i in range(len(words)):
    print(words[i], ":", stemmed_words[i])
