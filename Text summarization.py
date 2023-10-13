import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
def simple_text_summarizer(text, num_sentences=3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]
    word_freq = FreqDist(words)
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence):
            if word in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word]
                else:
                    sentence_scores[sentence] += word_freq[word]
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return ' '.join(summary_sentences)
text = """
Natural Language Processing (NLP) is a subfield of artificial intelligence (AI) that focuses on the interaction
between computers and humans through natural language. NLP techniques are used in a wide range of applications, 
including text and speech recognition, language translation, sentiment analysis, and text summarization. 
Text summarization is the process of condensing a longer piece of text into a shorter version while retaining 
the key information and main ideas.
"""
summary = simple_text_summarizer(text, num_sentences=2)
print(summary)