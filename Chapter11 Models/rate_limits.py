import backoff 
import openai
import config
from openai import OpenAI
client = OpenAI(api_key=config.API_KEY)

@backoff.on_exception(backoff.expo, openai.RateLimitError)
def completions_with_backoff(**kwargs):
    return client.completions.create(**kwargs)
 
completions_with_backoff(model="gpt-3.5-turbo-instruct", prompt="I was walking down the street,")
