from sklearn.feature_extraction.text import TfidfVectorizer

# Define the corpus
corpus = ['This is the first document.',
          'This is the second document.',
          'And this is the third one.',
          'Is this the first document?']

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Compute the TF-IDF scores
tfidf_matrix = vectorizer.fit_transform(corpus)

# Print the TF-IDF scores
print(tfidf_matrix.toarray())
