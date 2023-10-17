import re
text = "Software Testing is fun"
pattern = "Software testing"
match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found")

# Example 2: Using re.findall() to find all occurrences of a pattern in a string
text = "The quick brown fox jumps over the lazy dog"
pattern = r"\b\w{4}\b"  # Match four-letter words
matches = re.findall(pattern, text)
print("Matches:", matches)

# Example 3: Using re.match() to check if a pattern matches at the beginning of a string
text = "abcdef"
pattern = "c"
match = re.match(pattern, text)
if match:
    print("Pattern found at the beginning of the string:", match.group())
else:
    print("Pattern not found at the beginning of the string")
