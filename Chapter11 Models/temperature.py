from openai import OpenAI
import config

client = OpenAI(api_key=config.API_KEY)

# Define a function to generate a response from ChatGPT
def generate_response(prompt, temperature):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{prompt}"}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

# Prompt for the conversation
prompt = "Suggest 4 fast food company names."

# Generate a response with low temperature (more focused and deterministic)
for i in range(3):
    low_temp_response = generate_response(prompt, 0)
    print(f"Response with low temperature (0) {i}:\n", low_temp_response)

for i in range(3):
    # Generate a response with default temperature (balanced and creative)
    default_temp_response = generate_response(prompt, 1)
    print(f"Response with default temperature (1) {i}:\n", default_temp_response)
