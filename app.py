
from flask import Flask, render_template, session, request, redirect, url_for
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect(url_for("survey"))


@app.route("/survey")
def survey():
    return render_template('no_question.html', question="What will you choose?", option_1="Let Shinto salvage the pod", option_2="Retain ownership of the pod")
