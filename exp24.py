from dialogtag import DialogTag

# Define the dialog
dialog = [
    ("Hello, how can I help you?", "greeting"),
    ("I'm looking for a book on Python programming.", "request"),
    ("Sure, we have several books on Python programming. Do you have a specific title in mind?", "query"),
    ("No, I'm open to suggestions.", "inform"),
    ("How about 'Python for Data Science'?", "suggest"),
    ("That sounds interesting. Can you tell me more about it?", "query"),
    ("Certainly. 'Python for Data Science' is a comprehensive guide to using Python for data analysis and visualization.", "inform"),
    ("Great, I'll take it.", "inform"),
    ("Okay, that will be $29.99. Would you like to pay with cash or credit?", "request")
]

# Create a DialogTag object
dialogtag = DialogTag()

# Recognize the dialog acts
for utterance, dialog_act in dialog:
    predicted_dialog_act = dialogtag.predict(utterance)
    if predicted_dialog_act == dialog_act:
        print(f"Correctly predicted {dialog_act} for utterance: {utterance}")
    else:
        print(f"Incorrectly predicted {predicted_dialog_act} for utterance: {utterance}")
