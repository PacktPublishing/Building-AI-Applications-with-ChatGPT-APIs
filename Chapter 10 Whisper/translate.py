import openai
import config

# API Token
openai.api_key = config.API_KEY

whisper_file= open("files/german.mp3", "rb")
result = openai.Audio.translate("whisper-1", whisper_file)
print(result)