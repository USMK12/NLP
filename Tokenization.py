import nltk

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

# Get user input
user_input = input("Enter a sentence: ")

# Tokenize the input
tokens = nltk.word_tokenize(user_input)

print("Tokens:")
print(tokens)
