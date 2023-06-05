import openai # for making OpenAI API requests

import config

# Set up OpenAI API credentials
openai.api_key = config.API_KEY

num_stories = 10
prompts = ["I was walking down the street and"] * num_stories

# Perform batched completions with 10 stories per request
response = openai.Completion.create(
            model="curie",
            prompt=prompts,
            max_tokens=20,
            )

# Match completions to prompts by index
stories = [""] * len(prompts)
for choice in response.choices:
    stories[choice.index] = prompts[choice.index] + choice.text

# Print the generated stories
for story in stories:
    print(story)
