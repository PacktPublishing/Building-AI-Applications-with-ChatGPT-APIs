from openai import OpenAI
import config
client = OpenAI(api_key=config.API_KEY)

# Define a function for chat completion
def chat_with_model(messages):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content

# Define the conversation messages
messages = [
    {"role": "user", "content": "Hello, could you recommend a good book to read?"},
    {"role": "assistant", "content": "Of course! What genre are you interested in?"},
    {"role": "user", "content": "I enjoy fantasy novels."},
    {"role": "assistant", "content": "Great! I recommend 'The Name of the Wind' by Patrick Rothfuss."},
    {"role": "user", "content": "Thank you! Can you tell me a bit about the plot?"},
]

# Chat with the model
response = chat_with_model(messages)
print(response)
