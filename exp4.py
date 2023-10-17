import re

def pluralize(word):
    # Define the pluralization rules
    rules = [
        ['[sxz]$', '$', 'es'],
        ['[^aeioudgkprt]h$', '$', 'es'],
        ['(qu|[^aeiou])y$', 'y$', 'ies'],
        ['$', '$', 's']
    ]

    # Apply the rules in order
    for rule in rules:
        pattern, search, replace = rule
        if re.search(pattern, word):
            return re.sub(search, replace, word)

# Example usage
print(pluralize("cat"))  # cats
print(pluralize("dog"))  # dogs
print(pluralize("knife"))  # knives
print(pluralize("potato"))  # potatoes
