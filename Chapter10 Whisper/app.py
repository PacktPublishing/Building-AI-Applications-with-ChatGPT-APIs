import tkinter as tk
from tkinter import filedialog
from openai import OpenAI
import config

# API Token
client = OpenAI(api_key=config.API_KEY)

def transcribe_audio():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        try:
            audio_file = open(file_path, "rb")
            transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
            text_window.insert(tk.END, transcript.text)
        except Exception as e:
            text_window.insert(tk.END, f"Error: {str(e)}")
    else:
        text_window.insert(tk.END, "No file selected.")

# Create the Tkinter window
window = tk.Tk()
window.title("Chapter 10 Whisper Transcription App")

# Create a text window
text_window = tk.Text(window, height=30, width=60)
text_window.pack()

# Create a button to select the audio file
button = tk.Button(window, text="Select Audio File", command=transcribe_audio)
button.pack()

# Start the Tkinter event loop
window.mainloop()
