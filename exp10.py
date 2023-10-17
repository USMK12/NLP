import nltk
from nltk.tag import BrillTagger
from nltk.corpus import treebank

# Download the Treebank corpus
nltk.download('treebank')

# Get the tagged sentences from the Treebank corpus
tagged_sentences = treebank.tagged_sents()

# Define the transformation rules
rules = [
    nltk.tag.brill.SymmetricProximateTokensTemplate(nltk.tag.brill.ProximateTagsRule, (1,1)),
    nltk.tag.brill.SymmetricProximateTokensTemplate(nltk.tag.brill.ProximateTagsRule, (2,2)),
    nltk.tag.brill.SymmetricProximateTokensTemplate(nltk.tag.brill.ProximateTagsRule, (1,2)),
    nltk.tag.brill.SymmetricProximateTokensTemplate(nltk.tag.brill.ProximateWordsRule, (1,1)),
    nltk.tag.brill.SymmetricProximateTokensTemplate(nltk.tag.brill.ProximateWordsRule, (2,2)),
    nltk.tag.brill.SymmetricProximateTokensTemplate(nltk.tag.brill.ProximateWordsRule, (1,2)),
    nltk.tag.brill.ProximateTagsRule(nltk.probability.FreqDist(), 1),
    nltk.tag.brill.ProximateTagsRule(nltk.probability.FreqDist(), 2),
    nltk.tag.brill.ProximateWordsRule(nltk.probability.FreqDist(), 1),
    nltk.tag.brill.ProximateWordsRule(nltk.probability.FreqDist(), 2)
]

# Train the tagger using the transformation rules and tagged sentences
tagger = BrillTagger.train(tagged_sentences, rules=rules)

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
