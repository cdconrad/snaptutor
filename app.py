import os

from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get(".env"),
)

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        reflection = request.form["reflection"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.6,
            messages=[
                {"role": "system","content": "Students will provide you with short reflections on emerging trends in the business world. Evaluate the reflections in terms of the following: evidence of critical thought, proficiency with business or technology concepts. Provide a written explanation of your evaluation that is between 10 and 50 words long. Conclude with an overall evaluation between 1 and 5 where 1 represents very poor performance and 5 represents excellent performance."},
                {"role": "user", "content": reflection}
            ]
        )
        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)