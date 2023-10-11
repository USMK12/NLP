import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Get input text from the user
text = input("Enter a sentence: ")

# Tokenize the input text
words = word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Perform part-of-speech tagging on the remaining words
pos_tags = pos_tag(filtered_words)

# Print the tagged words
for word, pos_tag in pos_tags:
    print(f"Word: {word}, POS Tag: {pos_tag}")
