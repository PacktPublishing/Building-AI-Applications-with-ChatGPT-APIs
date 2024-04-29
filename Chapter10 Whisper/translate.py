from openai import OpenAI
import config

# API Token
client = OpenAI(api_key=config.API_KEY)

whisper_file= open("files/german.mp3", "rb")
result = client.audio.translations.create(model="whisper-1", file=whisper_file)
print(result)
