import sqlite3
from openai import OpenAI
from . import config

# API Token
client = OpenAI(
  api_key=config.API_KEY,
)

def initialize_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions
                      (id INTEGER PRIMARY KEY, key TEXT UNIQUE, value TEXT)''')
    conn.commit()
    conn.close()

def generate_questions(text):
    initialize_database()
    # Connect to the SQLite database
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    # Define your prompt for generating questions
    prompt = f"Create a practice test with multiple choice questions on the following text:\n{text}\n\n" \
             f"Each question should be on a different line. Each question should have 4 possible answers. " \
             f"Under the possible answers we should have the correct answer."

    # Generate questions using the ChatGPT API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{prompt}"}],
        max_tokens = 3500,
        stop = None,
        temperature = 0.7
    )

    # Extract the generated questions from the API response
    questions = response.choices[0].message.content

    # Generate a unique key for the question
    base_key = ' '.join(text.split()[:2])
    key = base_key
    index = 1
    while key_exists(cursor, key):
        key = f"{base_key} {index}"
        index += 1

    # Insert the questions into the database
    value = questions
    cursor.execute("INSERT INTO questions (key, value) VALUES (?, ?)", (key, value))
    conn.commit()

    return questions

def key_exists(cursor, key):
    cursor.execute("SELECT COUNT(*) FROM questions WHERE key = ?", (key,))
    count = cursor.fetchone()[0]
    return count > 0

def print_all_questions():
    initialize_database()
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    # Retrieve all rows from the database
    cursor.execute("SELECT * FROM questions")
    rows = cursor.fetchall()
    return rows

