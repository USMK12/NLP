import spacy

# Load the English language model
nlp = spacy.load("en")

# Get user input
user_input = input("Enter a sentence: ")

# Process the input using spaCy
doc = nlp(user_input)

# Generate the parse tree
for token in doc:
    print(f"{token.text} ({token.dep_} -> {token.head.text})")
  
