from textblob import TextBlob
text = "I love this product! It's amazing."

analysis = TextBlob(text)
sentiment = analysis.sentiment

polarity = sentiment.polarity
subjectivity = sentiment.subjectivity

print(f"Polarity: {polarity}")
print(f"Subjectivity: {subjectivity}")

if polarity > 0:
    print("The text is positive.")
elif polarity < 0:
    print("The text is negative.")
else:
    print("The text is neutral.")
