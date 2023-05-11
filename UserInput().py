import openai
import time

# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = "  "

# Define the OpenAI model ID you want to use
model_engine = "   "


# Define a function to generate the response from the model
def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message


# Define a tuple of exit commands for the chat session
exit_commands = ("exit", "quit", "bye", "goodbye")

# Ask the user for a question
while True:
    question = input("Ask a question (type 'exit' to quit): ")
    if question.lower() == exit_commands:
        break

# Generate a response from ChatGPT
start = time.time()
response = generate_response(question)
end = time.time()

# Print the response and response time
print("Response:", response)
print("Response time:", round(end - start, 2), "seconds")
