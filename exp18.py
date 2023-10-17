import re

def parse_fopc(expression):
    # Remove whitespace
    expression = re.sub(r'\s', '', expression)

    # Check if the expression is a valid FOPC formula
    if not re.match(r'^[A-Za-z]+\(.+\)$', expression):
        raise ValueError('Invalid FOPC formula')

    # Split the expression into predicate and arguments
    predicate, arguments = re.split(r'\(|\)', expression)
    arguments = arguments.split(',')

    return {
        'predicate': predicate,
        'arguments': arguments
    }

# Test the parser
expression = 'P(x, y, z)'
parsed_expression = parse_fopc(expression)
print(parsed_expression)
