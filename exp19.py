import nltk
from nltk.corpus import wordnet as wn

def lesk(context_sentence, ambiguous_word, pos=None, synsets=None):
    if synsets is None:
        synsets = wn.synsets(ambiguous_word, pos=pos)

    context = set(context_sentence)
    best_sense = None
    max_overlap = 0

    for sense in synsets:
        signature = set(sense.definition().split())
        for example in sense.examples():
            signature.union(set(example.split()))

        overlap = len(context.intersection(signature))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense

# Example usage
sentence = ['I', 'went', 'to', 'the', 'bank', 'to', 'deposit', 'money', '.']
ambiguous_word = 'bank'
sense = lesk(sentence, ambiguous_word, pos='n')
print(sense)
