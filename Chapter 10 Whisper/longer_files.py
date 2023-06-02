import openai
from pydub import AudioSegment
import config

# API Token
openai.api_key = config.API_KEY

song = AudioSegment.from_mp3("files/phone.mp3")

# 5 minute portion
five_minutes = 5 * 60 * 1000
first_min_5 = song[:five_minutes]
first_min_5.export("files/phone_first_5.mp3", format="mp3")

last_min_5 = song[five_minutes:]
last_min_5.export("files/phone_last_5.mp3", format="mp3")

file= open("files/phone_first_5.mp3", "rb")
result = openai.Audio.transcribe("whisper-1", file)
print(result)

file= open("files/phone_last_5.mp3", "rb")
result = openai.Audio.transcribe("whisper-1", file)
print(result)