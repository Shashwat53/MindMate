import openai
import os
# Set up the OpenAI API key
openai.api_key = os.environ["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"]
# Define a function to generate a response using OpenAI's GPT-3 model
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message
# Define a function to handle user input and generate a response
def handle_input(input_text):
    prompt = f"User: {input_text}\nBot:"
    response = generate_response(prompt)
    return response
# Set up a loop to continually prompt the user for input and generate responses
while True:
    user_input = input("You: ")
    bot_response = handle_input(user_input)
    print(f"Bot: {bot_response}")
#API Key: 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