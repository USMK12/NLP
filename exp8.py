import nltk
from nltk.corpus import treebank

# Download the Treebank corpus
nltk.download('treebank')

# Get the tagged sentences from the Treebank corpus
tagged_sentences = treebank.tagged_sents()

# Create a frequency distribution of words and their corresponding tags
word_tag_freq = nltk.FreqDist((word.lower(), tag) for sentence in tagged_sentences for (word, tag) in sentence)

# Function to assign the most frequent tag to a given word
def get_most_frequent_tag(word):
    return word_tag_freq[word.lower()].max()

# Function to assign POS tags to a given sentence
def pos_tag(sentence):
    # Tokenize the sentence into words
    words = nltk.word_tokenize(sentence)

    # Assign POS tags to the words using the most frequent tag for each word
    tagged_words = [(word, get_most_frequent_tag(word)) for word in words]

    return tagged_words

# Test the POS tagging algorithm on a sample sentence
sentence = "The cat is sitting on the mat."
tagged_sentence = pos_tag(sentence)
print(tagged_sentence)
