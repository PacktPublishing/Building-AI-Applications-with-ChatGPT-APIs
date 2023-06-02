import openai
import config

# API Token
openai.api_key = config.API_KEY

file= open("files/apple.mp3", "rb")
result = openai.Audio.transcribe("whisper-1", file)
print(result)