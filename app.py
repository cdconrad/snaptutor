import os, sqlite3

from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get(".env"),
)

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        reflection = request.form["reflection"]
        option = request.form['options']
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.6,
            messages=[
                {"role": "system","content": "Students will provide you with short reflections on emerging trends in the business world. Evaluate the reflections in terms of the following: evidence of critical thought, proficiency with business or technology concepts. Provide a written explanation of your evaluation that is between 10 and 50 words long. Conclude with an overall evaluation between 1 and 5 where 1 represents very poor performance and 5 represents excellent performance."},
                {"role": "user", "content": reflection}
            ]
        )
        msg = response.choices[0].message.content
        conn = get_db_connection()
        conn.execute("INSERT INTO prompts (TextbookID, reflection, msg) VALUES (?, ?, ?)",
                     (option, reflection, msg))
        conn.commit()
        conn.close()
        return redirect(url_for("index", result=msg))

    result = request.args.get("result")
    return render_template("index.html", result=result)