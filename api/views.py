from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "you're welcome to ireporter"

