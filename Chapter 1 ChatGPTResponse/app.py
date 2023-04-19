import openai

# Use OpenAI API Key
openai.api_key= "<YOUR_API_KEY>"

# Ask the user for question
question = input("What would you Like to ask OpenAI? ")
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=question,
    max_tokens=512,
    n=1,
    stop=None,
    temperature=0.8,
)
print(response)
answer = response["choices"][0][ "text"]
print("OpenAI:" + answer)
