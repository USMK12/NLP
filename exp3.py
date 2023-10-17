import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize

def morphological_analysis(text):
    # Tokenization
    tokens = word_tokenize(text)

    # POS tagging
    pos_tags = nltk.pos_tag(tokens)

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag)) for word, tag in pos_tags]

    # Stemming
    stemmer = PorterStemmer()
    stems = [stemmer.stem(word) for word in tokens]

    return tokens, pos_tags, lemmas, stems

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif tag.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    elif tag.startswith('R'):
        return nltk.corpus.wordnet.ADV
    else:
        return nltk.corpus.wordnet.NOUN

# Example usage
text = "The quick brown fox jumps over the lazy dogs"
tokens, pos_tags, lemmas, stems = morphological_analysis(text)

print("Tokens:", tokens)
print("POS tags:", pos_tags)
print("Lemmas:", lemmas)
print("Stems:", stems)
