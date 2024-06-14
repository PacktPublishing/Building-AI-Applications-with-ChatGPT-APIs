"""
file name: app.py
Description: Building a ChatGPT Clone with Flask framework
__copyright__ = "Copyright 2024, MartinYTech"
__author__=  Martin Yanev
__modified__= 03/03/2024
"""

from flask import Flask, request, render_template
from openai import OpenAI
import config


client = OpenAI(api_key=config.API_KEY)
app = Flask(__name__)

conversation_history = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

    model_engine = "gpt-3.5-turbo"

    conversation_history.append({"role": "user", "content": userText})
    response = client.chat.completions.create(
        model=model_engine,
        messages=conversation_history
    )
    # Append AI response to conversation history
    ai_response = response.choices[0].message.content

    conversation_history.append({"role": "assistant", "content": ai_response})

    return ai_response


if __name__ == "__main__":
    app.run()
