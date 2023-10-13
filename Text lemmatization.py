from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
text = "The quick brown foxes are jumping over the lazy dogs"
words = nltk.word_tokenize(text)
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print(lemmatized_words)