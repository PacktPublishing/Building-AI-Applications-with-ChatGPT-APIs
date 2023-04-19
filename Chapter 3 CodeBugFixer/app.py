"""
file name: app.py
Description: Building a Code Bug Fixer App with ChatGPT API
__copyright__ = "Copyright 2023, MartinYTech"
__author__=  Martin Yanev
__modified__= 09/04/2023
"""

from flask import Flask, request, render_template
import openai
import config

app = Flask(__name__)

# API Token
openai.api_key = config.API_KEY

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Code Errr
        code = request.form["code"]
        error = request.form["error"]

        prompt = (f"Explain the error in this code without fixing it:"
                  f"\n\n{code}\n\nError:\n\n{error}")
        model_engine = "text-davinci-003"
        explanation_completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.9,
        )

        explanation = explanation_completions.choices[0].text
        print(explanation)
        fixed_code_prompt = (f"Fix this code: \n\n{code}\n\nError:\n\n{error}."
                             f" \n Respond only with the fixed code.")
        fixed_code_completions = openai.Completion.create(
            engine=model_engine,
            prompt=fixed_code_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.9,
        )
        fixed_code = fixed_code_completions.choices[0].text

        return render_template("index.html",
                               explanation=explanation,
                               fixed_code=fixed_code)

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
