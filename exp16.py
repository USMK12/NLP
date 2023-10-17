import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define the text to be analyzed
text = "Apple is looking at buying U.K. startup for $1 billion"

# Process the text
doc = nlp(text)

# Print the named entities and their labels
for ent in doc.ents:
    print(ent.text, ent.label_)
