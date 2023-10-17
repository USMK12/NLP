import openai
import os

# Set up the OpenAI API
openai.api_key = os.environ['OPENAI_API_KEY']

# Load the GPT-3 model
model_engine = "text-davinci-002"
model = openai.Model(model_engine)

# Define the prompt
prompt = "Write a short story about a robot that learns to love."

# Generate text from the prompt
response = model.generate(prompt, max_tokens=1024)

# Print the generated text
print(response.choices[0].text)
