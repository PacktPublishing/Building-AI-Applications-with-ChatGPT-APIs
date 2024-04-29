from openai import OpenAI
import config

# API Token
client = OpenAI(api_key=config.API_KEY)

file= open("files/apple.mp3", "rb")
result = client.audio.transcriptions.create(model="whisper-1", file=file)
print(result)
