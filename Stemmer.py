import nltk
from nltk.stem import PorterStemmer

# Download the NLTK data
nltk.download('punkt')

# Create a stemmer object
stemmer = PorterStemmer()

# Get user input
user_input = input("Enter a sentence: ")

# Tokenize the input sentence
words = nltk.word_tokenize(user_input)

# Apply stemming to each word
stemmed_words = [stemmer.stem(word) for word in words]

# Join the stemmed words to form a sentence
stemmed_sentence = ' '.join(stemmed_words)

print("Stemmed sentence:", stemmed_sentence)
