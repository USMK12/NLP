import nltk
from nltk.tag import RegexpTagger

# Define the patterns for tagging
patterns = [
    (r'\d+', 'CD'),  # Match numbers
    (r'.*ing$', 'VBG'),  # Match words ending with -ing
    (r'.*ed$', 'VBD'),  # Match words ending with -ed
    (r'.*ness$', 'NN'),  # Match words ending with -ness
    (r'.*ful$', 'JJ')  # Match words ending with -ful
]

# Load the Treebank corpus for training and testing
nltk.download('treebank')
train_data = nltk.corpus.treebank.tagged_sents()[:3000]
test_data = nltk.corpus.treebank.tagged_sents()[3000:]

# Train the tagger using the training data and patterns
tagger = RegexpTagger(patterns)
tagger.train(train_data)

# Evaluate the tagger using the testing data
accuracy = tagger.evaluate(test_data)
print("Accuracy:", accuracy)

# Test the tagger on some example sentences
sentences = [
    "I have 3 cats.",
    "She is running.",
    "The weather is beautiful.",
    "His kindness is appreciated."
]

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tagged_words = tagger.tag(words)
    print(tagged_words)
