import random
import nltk
from nltk.tokenize import word_tokenize

# Load the text data
text = "I am a big fan of natural language processing. It is a fascinating field with many applications."

# Tokenize the text into words
tokens = word_tokenize(text)

# Create a bigram model
bigrams = list(nltk.bigrams(tokens))

# Create a dictionary to store the bigram frequencies
model = {}
for w1, w2 in bigrams:
    if w1 in model:
        model[w1].append(w2)
    else:
        model[w1] = [w2]

# Generate text using the bigram model
seed = random.choice(tokens)
generated_text = [seed]
for _ in range(10):
    current_word = generated_text[-1]
    next_word = random.choice(model[current_word])
    generated_text.append(next_word)

# Join the generated words into a sentence
generated_sentence = ' '.join(generated_text)

# Print the generated sentence
print(generated_sentence)
