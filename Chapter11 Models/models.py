import openai
import config

# Define the prompt and test questions
prompt = "Estimate the square root of 121 and type a 'orange' after every digit of the square root"

# Set up OpenAI API credentials
openai.api_key = config.API_KEY

# Define the model names and their corresponding IDs
model_ids = {
    "DAVINCI 003": {"model": "text-davinci-003", "cost": 0.02},
    "DAVINCI 002": {"model": "text-davinci-002", "cost": 0.02},
    "DAVINCI": {"model": "davinci", "cost": 0.02},
    "GPT3.5 TURBO": {"model": "gpt-3.5-turbo", "cost": 0.002},
    "GPT3.5 TURBO 0301": {"model": "gpt-3.5-turbo-0301", "cost": 0.002},
    "GPT4": {"model": "gpt-4", "cost": 0.0045},
    "CURIE": {"model": "text-curie-001", "cost": 0.002},
    "BABBAGE": {"model": "text-babbage-001", "cost": 0.005},
}

# Make API calls to the models and store the responses
responses = {}
for model_name, model_id in model_ids.items():
    if "GPT" not in model_name:
        response = openai.Completion.create(
            engine=model_id["model"],
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7
        )
        responses[model_name] = [response.choices[0].text.strip(),
                                 response['usage']['total_tokens']/1000*model_id["cost"]]

    else:
        response = openai.ChatCompletion.create(
            model=model_id["model"],
            messages=[
                {"role": "user", "content": "I will ask you a question"},
                {"role": "assistant", "content": "Ok"},
                {"role": "user", "content": f"{prompt}"}
            ]
        )
        responses[model_name] = [response["choices"][0]["message"]["content"],
                                 response['usage']['total_tokens']/1000*model_id["cost"]]


for model, response in responses.items():
    print(f"{model}: {response[0]}")
    print(f"{model} COST: {response[1]}")
