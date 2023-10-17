from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the English-to-French translation model
model_checkpoint = "Helsinki-NLP/opus-mt-en-fr"
model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)

# Tokenize the English text
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
english_text = "Hello, how are you?"
english_tokens = tokenizer(english_text, return_tensors="pt")

# Translate the English text to French
french_tokens = model.generate(**english_tokens, max_length=128, num_beams=4, early_stopping=True)
french_text = tokenizer.decode(french_tokens[0], skip_special_tokens=True)

# Print the translated French text
print(french_text)
