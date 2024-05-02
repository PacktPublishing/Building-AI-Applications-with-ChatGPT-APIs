from openai import OpenAI

import config

client = OpenAI(api_key=config.API_KEY)

# Define a function to generate a response from ChatGPT
def generate_response(prompt, n):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{prompt}"}
        ],
        n=n,
        temperature=1
    )
    return response

# Prompt for the conversation
prompt = "Suggest 4 names for a cat."

n_prompt = generate_response(prompt, 4)
print(n_prompt)
for choice in n_prompt.choices:
    print(f"-------------------------")
    print(f"Choice: {choice}")
    print(choice.message.content)

print(f"-------------------------")

