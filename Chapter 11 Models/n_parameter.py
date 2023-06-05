import openai
import config

# Set up OpenAI API credentials
openai.api_key = config.API_KEY

# Define a function to generate a response from ChatGPT
def generate_response(prompt, n):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=.8,
        max_tokens=50,
        n=n,
        stop=None,
    )
    return response

# Prompt for the conversation
prompt = "Suggest 4 names for a cat."


n_prompt = generate_response(prompt, 4)
print(n_prompt)
