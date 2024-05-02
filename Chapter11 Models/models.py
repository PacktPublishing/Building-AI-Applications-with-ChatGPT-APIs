from openai import OpenAI
import config

client = OpenAI(api_key=config.API_KEY)

# Define the prompt and test questions
prompt = "Estimate the square root of 121 and type 'orange' after every digit of the square root result"

# Define the model names and their corresponding IDs
model_ids = {
    "GPT3.5 TURBO": {"model": "gpt-3.5-turbo", "cost": 1.00},
    "GPT3.5 TURBO 0125": {"model": "gpt-3.5-turbo-0125", "cost": 1.00},
    "GPT4": {"model": "gpt-4", "cost": 45.00},
    "GPT4 TURBO": {"model": "gpt-4-turbo", "cost": 20.00},
}

# Make API calls to the models and store the responses
responses = {}
for model_name, model_id in model_ids.items():
    response = client.chat.completions.create(
        model=model_id["model"],
        messages=[
            {"role": "user", "content": f"{prompt}"}
        ]
    )
    responses[model_name] = [response.choices[0].message.content,
                             response.usage.total_tokens * (model_id["cost"]/1000000)]

for model, response in responses.items():
    print("\n----------------------------------------")
    print(f"{model}: {response[0]}")
    print(f"{model} COST: {response[1]}")

print("----------------------------------------")




for model, response in responses.items():
    print(f"{model}: {response[0]}")
    print(f"{model} COST: {response[1]}")
